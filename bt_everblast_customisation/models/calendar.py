from odoo import api, fields, models, _


class Meeting(models.Model):
    _inherit = 'calendar.event'
    
    animator_id = fields.Many2one('product.product', string='Animator')
    equipment_id = fields.Many2one('product.product', string='Equipment')
    product_id = fields.Many2one('product.product', string='Product')
    order_line_id = fields.Many2one('sale.order.line', string='Sale Order Line')
    