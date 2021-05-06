# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# from odoo.addons.http_routing.models.ir_http import slug
import json
from odoo import http, _
from datetime import datetime, timedelta
# from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
from odoo.http import request
from werkzeug.exceptions import NotFound
from odoo.exceptions import ValidationError
from odoo.addons.website_form.controllers.main import WebsiteForm





class CampRegistration(http.Controller):
     
    @http.route(['/campregistration'], type='http', auth="public", website=True)
    def campregistration(self, **kwargs):
        
        render_values = {
            'states': request.env['res.country.state'].sudo().search([]),
            'weeks': request.env['camp.week.selection'].sudo().search([]),
            }
        return request.render("camp_registration.camp_registration_form", render_values)


class WebsiteForm(WebsiteForm):
    

    def validate(self, date_text):
        try:
            if date_text != datetime.strptime(date_text, "%Y-%m-%d %H:%M:%S").strftime('%Y-%m-%d %H:%M:%S'):
                raise ValueError
            return True
        except ValueError:
            return False
        
    def extract_data(self, model, values):
        peoples = ['_1', '_2', '_3', '_4', '_5']
        ppls = []
        for people in peoples:
            people_data = {k.split(people)[0] : v for k, v in values.items() if k.endswith(people)}
            if people_data:
                ppls.append((0, 0, people_data))
        
        date_list = []
        check_same_date_slot = []     
        am_slots = ['1_am', '2_am', '3_am', '4_am', '5_am']
        for am_slot in am_slots:
            am_slot_data = {k.split('_')[0] : v for k, v in values.items() if k.startswith(am_slot)}
            if am_slot_data:
                for week_ids in am_slot_data.values():
                    week_ids=list(week_ids)
                    for week_id in week_ids:
                        if week_id.isdigit():
                            week = request.env['camp.week.selection'].sudo().browse(int(week_id))
                            date1 = week.date_from
                            date2 = week.date_to
                            day = int(am_slot.split('_')[0])
                            date = date1 + timedelta(days=(day-1))
                            date_vals = {
                                'week_id': week.id,
                                'date': date,
                                'slot': 'AM'
                            }
                            date_list.append((0, 0,date_vals))
                            check_same_date_slot.append(date)

        pm_slots = ['1_pm', '2_pm', '3_pm', '4_pm', '5_pm']
        for pm_slot in pm_slots:
            pm_slot_data = {k.split('_')[0] : v for k, v in values.items() if k.startswith(pm_slot)}
            if pm_slot_data:
                for week_ids in pm_slot_data.values():
                    week_ids=list(week_ids)
                    for week_id in week_ids:
                        if week_id.isdigit():
                            week = request.env['camp.week.selection'].sudo().browse(int(week_id))
                            date1 = week.date_from
                            date2 = week.date_to
                            day = int(pm_slot.split('_')[0])
                            date = date1 + timedelta(days=(day-1))
                            date_vals = {
                                'week_id': week.id,
                                'date': date,
                                'slot': 'PM'
                            }
                            date_list.append((0, 0,date_vals))
                            check_same_date_slot.append(date)

        full_slots = ['1_full', '2_full', '3_full', '4_full', '5_full']
        for full_slot in full_slots:
            full_slot_data = {k.split('_')[0] : v for k, v in values.items() if k.startswith(full_slot)}
            if full_slot_data:
                for week_ids in full_slot_data.values():
                    week_ids=list(week_ids)
                    for week_id in week_ids:
                        if week_id.isdigit():
                            week = request.env['camp.week.selection'].sudo().browse(int(week_id))
                            date1 = week.date_from
                            date2 = week.date_to
                            day = int(full_slot.split('_')[0])
                            date = date1 + timedelta(days=(day-1))
                            date_vals = {
                                'week_id': week.id,
                                'date': date,
                                'slot': 'full'
                            }
                            date_list.append((0, 0,date_vals))
                            check_same_date_slot.append(date)
                            
#         if check_same_date_slot and len(check_same_date_slot) != len(set(check_same_date_slot)):
#             print('ssssssssssssssssssssssss',len(check_same_date_slot),len(set(check_same_date_slot)))
#             return {
#                 'error': {
#                     'title': _('Value Error'),
#                     'message': _('Select one slot(AM/PM/Fullday) per date'),
#                 }
#             }   
                       
        dob = ''
        if values.get('child_dob',  'False'):
            if values['child_dob']:
                dob = values['child_dob']
                del values['child_dob']
        
        camp_first_date = ''
        if values.get('camp_first_date',  'False'):
            if values['camp_first_date']:
                camp_first_date = values['camp_first_date']
                del values['camp_first_date']
#         if values.get('dietary_restrictions',  ''):
#             print('ddddddddddddddddd',values.get('dietary_restrictions',  ''))
#             dob = values['child_dob']
#             del values['child_dob']
                
        res = super(WebsiteForm, self).extract_data(model, values)
        res['record'].update({'pick_up_people_ids': ppls, 'camp_date_selection_ids': date_list})
        if dob:
            res['record'].update({'child_dob' : dob})
        if camp_first_date:
            res['record'].update({'camp_first_date' : camp_first_date})
        
        return res
    
    def insert_record(self, request, model, values, custom, meta=None):
        if custom or meta:
            custom = meta = ''
        res = super(WebsiteForm, self).insert_record(request, model, values, custom, meta=meta)
        return res

