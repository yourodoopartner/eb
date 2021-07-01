from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    event_date = fields.Date(string='Event Date')
    
    animator_id = fields.Many2one('product.product', string='Animator')
    
    
    def _prepare_invoice(self):
        self.ensure_one()
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        if self.event_date:
            invoice_vals.update({
                'event_date': self.event_date,
            })
        return invoice_vals
