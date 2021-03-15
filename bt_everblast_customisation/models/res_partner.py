# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    import_id = fields.Integer(string='Import ID')
    balance_owing = fields.Float(string='Balance Owing')
    
    