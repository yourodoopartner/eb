# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# from odoo.addons.http_routing.models.ir_http import slug
import json
from odoo import http, _
from datetime import datetime
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
        dob = ''
        if values.get('child_dob',  'False'):
            if values['child_dob']:
                dob = values['child_dob']
                del values['child_dob']
#         if values.get('dietary_restrictions',  ''):
#             print('ddddddddddddddddd',values.get('dietary_restrictions',  ''))
#             dob = values['child_dob']
#             del values['child_dob']
                
        res = super(WebsiteForm, self).extract_data(model, values)
        res['record'].update({'pick_up_people_ids': ppls})
        if dob:
            res['record'].update({'child_dob' : dob})
        
        return res
    
    def insert_record(self, request, model, values, custom, meta=None):
        if custom or meta:
            custom = meta = ''
        res = super(WebsiteForm, self).insert_record(request, model, values, custom, meta=meta)
        return res

