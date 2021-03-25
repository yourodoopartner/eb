from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    event_date = fields.Date(string='Event Date')