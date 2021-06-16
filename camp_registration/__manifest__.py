# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2017 BroadTech IT Solutions Pvt Ltd
#    (<http://broadtech-innovations.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Camp Registration',
    'version': '0.2',
    'category': 'custom',
    'summary': 'Camp Registration',
    'description': """
        Camp Registration""",
    'author' : 'BroadTech IT Solutions Pvt Ltd',
    'website' : 'http://www.broadtech-innovations.com',
    'depends': ['website_form', 'sale', 'odoo_rental_request_management'],
    'images': [],
    'data': [
        'data/camp_registration_data.xml',
        'security/ir.model.access.csv',
        'views/camp_registration_portal_view.xml',
        'views/camp_registration_view.xml',
        'views/thankspage.xml',
        'views/sale_view.xml',
        ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=2:softtabstop=2:shiftwidth=2:
