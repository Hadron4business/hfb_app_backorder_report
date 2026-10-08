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
"""	@version	20.0.1.0.0
	@owner  Hadron for Business
	@author Hadron for Business sp. z o.o.
	@date   2026.10.08

	Backorder Report - settings
	Exposes the company switch in Inventory > Configuration > Settings, with a
	link to the schedule.
"""
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    backorder_report = fields.Boolean(related='company_id.backorder_report', readonly=False)

    def action_open_backorder_cron(self):
        cron = self.env.ref('hfb_app_backorder_report.ir_cron_backorder_report')
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'ir.cron',
            'res_id': cron.id,
            'view_mode': 'form',
            'target': 'current',
        }

#EoF
