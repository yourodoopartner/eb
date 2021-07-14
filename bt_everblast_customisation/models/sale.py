
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    event_date = fields.Date(string='Event Date')
    animator_id = fields.Many2one('product.product', string='Animator')
    equipment_id = fields.Many2one('product.product', string='Equipment')
    
    
    def _prepare_invoice(self):
        self.ensure_one()
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        if self.event_date:
            invoice_vals.update({
                'event_date': self.event_date,
            })
        return invoice_vals
    
    def _action_confirm(self):
        for order in self:
            if order.is_custom_rental_quote:
                order.order_line._action_create_calendar_event()
        return super(SaleOrder, self)._action_confirm()
    
    def action_view_meeting(self):
        """ Open meeting's calendar view.
        """
        self.ensure_one()
        action = self.env.ref('calendar.action_calendar_event').read()[0]
        attendee_ids = self.env.user.partner_id.ids
        if self.partner_id:
            attendee_ids.append(self.partner_id.id)
        if self.user_id:
            attendee_ids.append(self.user_id.partner_id.id)
        action['context'] = {
            'default_partner_id': self.partner_id.id,
            'default_partner_ids': attendee_ids,
            'default_team_id': self.team_id.id,
        }
        action['domain'] = [('order_line_id', 'in', self.order_line.ids)]
        return action
    
    
   
class SaleOrderLine(models.Model):
    _inherit = "sale.order.line" 
    
    def _action_create_calendar_event(self):
        for line in self:
            if not line.custom_start_datetime or not line.custom_end_datetime:
                raise UserError(_('Please add Rental start and end dates for order lines.'))
            
            attendee_ids = self.env.user.partner_id.ids
            if line.order_id.partner_id:
                attendee_ids.append(line.order_id.partner_id.id)
            if line.order_id.user_id:
                attendee_ids.append(line.order_id.user_id.partner_id.id)
            
            calendar_vals = {
                'res_model_id': self.env.ref('sale.model_sale_order_line').id,
                'res_id': line.id,
                'order_line_id': line.id,
                'name': line.name,
                'partner_id': line.order_id.partner_id and line.order_id.partner_id.id or False,
                'partner_ids': [(6, 0, attendee_ids)],
                'start': line.custom_start_datetime,
                'stop': line.custom_end_datetime,
                'animator_id': line.order_id.animator_id and line.order_id.animator_id.id or False,
                'equipment_id': line.order_id.equipment_id and line.order_id.equipment_id.id or False,
                'product_id': line.product_id and line.product_id.id or False,
                }
            self.env['calendar.event'].create(calendar_vals)
        
    
    
    
    
    
    
    
    
    
