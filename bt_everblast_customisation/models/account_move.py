# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = "account.move"
    
    visible_pay_now = fields.Boolean(string='Gets PAY NOW button', help="Gets PAY NOW button in the invoice preview.")
