# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2018 BroadTech IT Solutions Pvt Ltd 
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
import io
import base64
import zipfile
import os.path
from contextlib import closing

import odoo
from odoo import api, fields, models, _, registry
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT,float_round
from odoo.exceptions import UserError, ValidationError


        
class AccountPrintPartnerDue(models.TransientModel):
    _name = "bt.print.partner.due"
    _description = "Account Print Partner Due"
    
    date = fields.Date('Date', default=fields.Date.context_today)
    partner_due_report_file = fields.Binary('Partner Due Report')
    file_name = fields.Char('File Name')
    partner_due_printed = fields.Boolean('Partner Due Report Printed')

    
    def generate_archive(self):
        """ Returns a zip file containing the given module with the given data. """
        
        report = self.env.ref('bt_partner_due.bt_partner_due_report')
        
        for wizard in self:
            domain = [
                ('state', '=', 'posted'), 
                ('invoice_payment_state', '=', 'not_paid'), 
                ('type', '=', 'out_invoice'), 
                ('invoice_date', '<=', wizard.date)]
            inv_partner_obj = [ inv_obj.partner_id for inv_obj in self.env['account.move'].search(domain)]
            inv_partner_obj = list(set(inv_partner_obj))
            with closing(io.BytesIO()) as f:
                with zipfile.ZipFile(f, 'w') as archive:
                    for partner_obj in inv_partner_obj:
                        if report.report_type in ['qweb-html', 'qweb-pdf']:
                            result, format = report.with_context(statement_date=wizard.date).render_qweb_pdf(partner_obj.id)
                        else:
                            res = report.render([partner_obj.id])
                            if not res:
                                raise UserError(_('Unsupported report type %s found.') % report.report_type)
                            result, format = res
        
                        report_name = (partner_obj.name).replace(' ','_') + ('_Due_Report')
                        ext = "." + format
                        if not report_name.endswith(ext):
                            report_name += ext
                            
                        archive.writestr(report_name, result)
                        
                excel_file = base64.encodestring(f.getvalue())
                wizard.partner_due_report_file = excel_file
                wizard.file_name = 'Partner_Due_Report_'+ wizard.date.strftime("%d_%m_%Y") + '.zip'
                wizard.partner_due_printed = True
                f.close()
                return {
                    'view_mode': 'form',
                    'res_id': wizard.id,
                    'res_model': 'bt.print.partner.due',                    
                    'type': 'ir.actions.act_window',
                    'context': self.env.context,
                    'target': 'new',
                    }
    
    
   

# vim:expandtab:smartindent:tabstop=2:softtabstop=2:shiftwidth=2: