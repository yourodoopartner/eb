# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "BT Partner Due Reports",
    "version": "1.1",
    "category": "Customization",
    "description": """
        This module will generate Partner Due Reports as zip
        """,
    "license": "LGPL-3",
    "summary": "Partner Due Reports",
    'sequence': 1,
    'author' : 'Your odoo partner',
    'website' : 'http://yourodoopartner.com/',
    "depends": [
        'account'
        ],
    "data": [
        'report/report_partner_due.xml',
        'views/report.xml',
        'wizard/print_partner_due_view.xml'
        ],
    'images': [],
    "installable": True,
    "auto_install": False,
}
# vim:expandtab:smartindent:tabstop=2:softtabstop=2:shiftwidth=2:
