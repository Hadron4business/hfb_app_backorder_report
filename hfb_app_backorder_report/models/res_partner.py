# -*- coding: utf-8 -*-
#################################################################################
#
# Odoo, Open Source Management Solution
# Copyright (C) 2017-2026 Hadron for Business sp. z o.o. (http://hadronforbusiness.com)
#
# This program is proprietary software, licensed under the Odoo Proprietary
# License v1.0 (OPL-1). Its use is governed by the Odoo Apps terms available
# at https://www.odoo.com/documentation/user/legal/licenses.html and the
# license agreement accepted at purchase / installation.
#
# It is forbidden to publish, distribute, sublicense, or sell copies of the
# Software or modified copies of the Software.
#
# The above copyright notice and this permission notice must be included in
# all copies or substantial portions of the Software.
#
#################################################################################
"""	@version	19.0.1.0.1
	@owner  Hadron for Business
	@author Hadron for Business sp. z o.o.
	@date   2026.10.08

	Backorder Report - customers
	Outgoing stock moves of a customer that are not delivered yet, the lines of
	the backorder e-mail, manual sending and the scheduled sending to every
	customer (with an e-mail and not excluded) of the companies that enabled the
	report.
"""
from odoo import _, api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    backorder_report_optout = fields.Boolean(
        string="No Backorder Report", help="Do not send the scheduled backorder report to this customer.")

    def _backorder_moves(self, company=None):
        """Outgoing stock moves of the commercial partner that are not delivered yet."""
        self.ensure_one()
        company = company or self.env.company
        return self.env['stock.move'].sudo().search([
            ('picking_id.partner_id', 'child_of', self.commercial_partner_id.id),
            ('picking_type_id.code', '=', 'outgoing'),
            ('state', 'not in', ('draft', 'done', 'cancel')),
            ('company_id', '=', company.id),
        ], order='date, id')

    def get_backorder_report_lines(self):
        """Lines of the backorder e-mail (used by the mail template)."""
        self.ensure_one()
        lang = self.lang or self.env.lang
        waiting = _("Waiting for stock")
        ready = _("Being prepared")
        return [{
            'order': move.picking_id.origin or move.picking_id.name,
            'product': move.product_id.with_context(lang=lang).display_name,
            'qty': move.product_uom_qty,
            'uom': move.product_uom.with_context(lang=lang).name,
            'date': move.date,
            'status': ready if move.state == 'assigned' else waiting,
        } for move in self._backorder_moves()]

    def action_send_backorder_report(self):
        template = self.env.ref('hfb_app_backorder_report.mail_template_backorder_report')
        return {
            'name': _("Send Backorder Report"),
            'type': 'ir.actions.act_window',
            'res_model': 'mail.compose.message',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_model': 'res.partner',
                'default_res_ids': self.commercial_partner_id.ids,
                'default_template_id': template.id,
                'default_composition_mode': 'comment',
            },
        }

    @api.model
    def _cron_send_backorder_report(self):
        template = self.env.ref('hfb_app_backorder_report.mail_template_backorder_report')
        for company in self.env['res.company'].search([('backorder_report', '=', True)]):
            moves = self.env['stock.move'].sudo().search([
                ('picking_type_id.code', '=', 'outgoing'),
                ('state', 'not in', ('draft', 'done', 'cancel')),
                ('company_id', '=', company.id),
                ('picking_id.partner_id', '!=', False),
            ])
            customers = moves.picking_id.partner_id.commercial_partner_id
            for customer in customers.filtered(lambda p: p.email and not p.backorder_report_optout):
                customer = customer.with_company(company).with_context(allowed_company_ids=[company.id])
                template.with_company(company).send_mail(customer.id)
                customer.message_post(body=_("Backorder report sent."))

#EoF
