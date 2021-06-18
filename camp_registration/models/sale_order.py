# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    camp_registration_id = fields.Many2one('camp.registration', string='Camp Registration Ref')
    camp_ref_code = fields.Char(string='Camp Code')
    
    child_name = fields.Char(string="Child's First Name")
    child_family_name = fields.Char(string="Child's Family Name")
    child_dob = fields.Date(string="Child's Date of Birth")
    
    parent_name = fields.Char(string='Parent/Guardian First Name')
    parent_family_name = fields.Char(string='Parent/Guardian Family Name')

    campreg_civic_number = fields.Char(string='Civic # & Street')
    campreg_city = fields.Char(string='City')
    campreg_postal_code = fields.Char(string='Postal Code')
    campreg_email = fields.Char(string='Email address')
    campreg_tele_phone = fields.Char(string="Telephone #")
    
    
    child_age = fields.Char(string='Age')
    child_gender = fields.Selection([('1', 'Male'),
                                     ('2', 'Female')], string='Gender', copy=False)
    
    emergancy_name = fields.Char(string='Emergency Contact Name')
    emergancy_contact_tele = fields.Char(string='Emergency Contact Telephone #')
    
    pick_up_people_ids = fields.One2many('pickup.people.details', 'sale_order_id', 'Pick up People Details',help="The following people are permitted to pick up this child from camp")
    
    dietary_restrictions = fields.Selection([('1', 'Yes'),
                                       ('0', 'No')], string='Dietary restrictions', default='0')
    dietary_restriction_details = fields.Text(string='Dietary restrictions Details')
    child_medical_condition = fields.Text(string='Medical Conditions/Allergies')
    
    campreg_comments = fields.Text(string='Additional Information / Comments')
    
    is_camp_organizer = fields.Boolean(string='Is camp organizer')
    camp_organizer = fields.Char(string='Camp Organizer Name')
    camp_organizer_phone = fields.Char(string="Camp Organizer Tel. #")
    camp_organizer_email = fields.Char(string='Camp Organizer Email address')
    
    camp_date_time = fields.Datetime(string='Date and Time')
    camp_host_name = fields.Char(string='Host First Name')
    camp_family_name = fields.Char(string='Host Family Name')
    camp_email = fields.Char(string='Host Email Address')
    camp_phone = fields.Char(string='Host Telephone #')
    camp_street = fields.Char(string='Civic # & Street')
    camp_city = fields.Char(string='City')
    camp_province = fields.Many2one('res.country.state',string='Province')
    camp_postal_code = fields.Char(string='Postal Code')
    camp_location = fields.Text(string='Our camp will take place at a park (indicate park name and address')
    camp_rain_plan = fields.Char(string='Rain Plan (garage, basement, other)')
    camp_first_date = fields.Date(string='First Date hosting this camp')
    
    is_more_camp_host = fields.Boolean(string='Our camp will have more than 1 host.')
    
    play_check = fields.Boolean(string='Are your kids allowed to play at the park? y/n')

    #marketting
    camp_condition_one = fields.Boolean(string='I have read and agree to the terms &amp; conditions and waiver of liability. ')
    camp_condition_two = fields.Boolean(string='I hereby grant permission to Everblast Backyard Camp to take photographs and video of my child to be used for promotional, instructional, educational or commercial purposes.')

    #terms and condition
    camp_terms_condition = fields.Html(string="Terms and conditions")
    
    camp_date_selection_ids = fields.One2many('camp.date.selection', 'sale_order_id', 'Camp Dates Selection')
    total_camp_days = fields.Float("Total Days", compute='_compute_total_days', store=True)
    
    
    animator = fields.Many2one('product.category', string='Animator')


    @api.depends('camp_date_selection_ids')
    def _compute_total_days(self):
        """
        Compute the total camp days.
        """
        for camp in self:
            total = 0
            for line in camp.camp_date_selection_ids:
                if line.slot == 'AM' or line.slot == 'PM':
                   total += 0.5
                elif line.slot == 'full':
                    total += 1
            camp.total_camp_days = total


