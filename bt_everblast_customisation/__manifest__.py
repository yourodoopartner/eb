# -*- coding: utf-8 -*-
{
    'name': "BroadTech Everblast Customisation",

    'summary': """
    BroadTech Everblast Customisation
    """,

    'description': """
    BroadTech Everblast Customisation
    """,

    'author': "Broadtech IT solutions pvt lmt",
    'website': "https://www.broadtech-innovations.com",

    'category': '',
    'version': '1.3',

    'depends': [
         'account_payment', 'sale', 'odoo_rental_request_management','calendar'
    ],

    'data': [
        'views/res_partner.xml',
        'views/product_view.xml',
        'views/sale_view.xml',
        'views/account_move_views.xml',
        'views/account_portal_templates.xml',
        'views/calendar_view.xml',
    ],

}
