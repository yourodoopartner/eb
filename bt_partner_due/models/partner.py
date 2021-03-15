# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _get_move_display_name(self, show_ref=False):
        self.ensure_one()
        return (self.name).replace(' ','_') + ('_Due_Report.pdf')
    
    
    def _get_report_base_filename(self):
        return self._get_move_display_name()
    
    
    def get_due_invoices(self):
        domain = [
            ('state', '=', 'posted'),
            ('invoice_payment_state', '=', 'not_paid'),
            ('partner_id', '=', self.id), 
            ('type', '=', 'out_invoice')
            ]
        if self._context.get('statement_date', False):
            domain.append(('invoice_date', '<=', self._context['statement_date']))
        return self.env['account.move'].search(domain)
        
# vim:expandtab:smartindent:tabstop=2:softtabstop=2:shiftwidth=2:
