# -*- coding: utf-8 -*-
# vim: tabstop=4 softtabstop=0 shiftwidth=4 smarttab expandtab fileformat=unix
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
{
    'name': "Backorder Report for Customers",
    'summary': "Automatically e-mail each customer the list of products still waiting to be delivered",
    'description': """
Backorder Report for Customers
==============================

When part of an order is still waiting for stock, customers do not know what
is still coming and when - so they call or write to the salesperson.

This app sends every customer, on a schedule (weekly by default), one e-mail
listing everything not yet delivered to them: order reference, product,
quantity and planned date. Customers with nothing pending get no e-mail.
Customers can be excluded one by one, the e-mail is an editable template,
and the report can also be sent manually from the customer.
""",
    'version': "20.0.1.0.0",
    'author': "Hadron for Business sp. z o.o.",
    'website': "http://hadronforbusiness.com",
    'license': "OPL-1",
    'category': "Inventory/Inventory",
    'depends': [
        'stock',
    ],
    'data': [
        'data/mail_template_data.xml',
        'data/ir_cron_data.xml',
        'views/res_config_settings_views.xml',
        'views/res_partner_views.xml',
    ],
    'images': [
        'static/description/banner_screenshot.png',
    ],
    'installable': True,
    'application': False,
}
