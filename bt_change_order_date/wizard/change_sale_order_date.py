# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class ChangeSaleOrderDate(models.TransientModel):
    _name = "sale.order.date.change"
    _description = "Change Sale Order Date"

    sale_order_date = fields.Datetime(string='Order Date', required=True, default=fields.Datetime.now)
    
    
    def change_sale_order_date(self):
        for wizard in self:
            sale_order_obj = self.env['sale.order'].browse(self._context.get('active_ids', []))
            old_date = sale_order_obj.date_order
            sale_order_obj.date_order = wizard.sale_order_date
            msg = "Order Date Changed : " + str(old_date) + " -> " + str(wizard.sale_order_date)
            sale_order_obj.message_post(body=msg)