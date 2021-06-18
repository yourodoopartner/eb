from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class PickupPeopleDetails(models.Model):
    _name = "pickup.people.details"
    _description = "Pickup People Details"

    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    camp_registration_id = fields.Many2one('camp.registration',string='Camp Registration')
    sale_order_id = fields.Many2one('sale.order', string='Rental Quote')
    
    
class CampWeekSelection(models.Model):
    _name = "camp.week.selection"
    _description = "Camp Week Selection"

    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    date_from = fields.Date(string='From Date')
    date_to = fields.Date(string='To Date')
    

class CampDateSelection(models.Model):
    _name = "camp.date.selection"
    _description = "Camp Date Selection"
    _order = 'date'

    name = fields.Char(string='Name')
    week_id = fields.Many2one('camp.week.selection',string='Week')
    date = fields.Date(string='Date')
    slot = fields.Selection([('AM', 'AM'), ('PM', 'PM'), ('full', 'Full Day')], string='Slot')
    camp_registration_id = fields.Many2one('camp.registration',string='Camp Registration')
    sale_order_id = fields.Many2one('sale.order', string='Rental Quote')
    
    
class Campregistration(models.Model):
    _name = "camp.registration"
    _description = "Camp Registration"
    
    
    @api.model
    def _update_ir_model(self):
        self.env.cr.execute("UPDATE ir_model_fields SET website_form_blacklisted=false WHERE model='camp.registration';")
        self.env.cr.execute("UPDATE ir_model SET website_form_access=true WHERE model='camp.registration';")
        
        
    agreemnet_terms = '''
    
    <li>Parent/guardian at host home is responsible for children immediately before and immediately after scheduled camp time.
    </li>
    <li>
    Children are not permitted to use swimming pools or enter swimming pool area.
    </li>
    <li>
    The directors reserve the right, at their discretion, to withdraw any camper whose influence or actions are deemed unsatisfactory, dangerous or incompatible to the Camp, or who will not live within the rules and policies of the Camp. If this occurs, no reduction or return of fee, or any part thereof will be made.
    </li>
    <li>
    In the event of an incident or an emergency, Backyard Camp staff are authorized to seek out and administer proper medical treatment to the best of their ability. Parents will be notified of all major and minor incidents in a timely manner.
    </li>
    <li>
    Rain/poor weather
    </n>
    In case of rain or poor weather, parents/guardians will have the option for camp to take place in an open garage, inside the house or move the replace the date with a future date.

    </li>
    <li>
    Waiver of Liability
    </n>
    While Everblast Backyard Camp's first concern is always the security and safety of the children, it, including its staff and administration, is not responsible for any and all claims of loss or damage, however caused, to any party or property, including the host's premises, arising directly or indirectly from participation in the Everblast Backyard camp.

    </li>
    <li>
    Covid-19
    </n>
    Everblast Backyard Camp will implement and respect all hygiene and physical distancing measures recommended by the Government of Quebec in order to limit the risk of transmission of COVID-19; however Everblast Backyard Camp does not guarantee that the children will not be exposed to or contract the virus.

    </li>
    <li>
    Campers will be sharing some of the same equipment, such as balls and other items, and will have to clean their hands before and after use of equipment.

    </li>
  


    '''
        
    ref_code = fields.Char(string='Camp Code')
    
    child_name = fields.Char(string="Child's First Name")
    child_family_name = fields.Char(string="Child's Family Name")
    child_dob = fields.Date(string="Child's Date of Birth")
    
    total_days = fields.Float(string="Total # Days")
    amount = fields.Float(string="Amount")
    
    parent_name = fields.Char(string='Parent/Guardian First Name')
    parent_family_name = fields.Char(string='Parent/Guardian Family Name')
    parent_social_insurance = fields.Char(string="Parent /Guardian's Social Insurance #")

    civic_number = fields.Char(string='Civic # & Street')
    city = fields.Char(string='City')
    postal_code = fields.Char(string='Postal Code')
    email = fields.Char(string='Email address')
    tele_phone = fields.Char(string="Telephone #")
    
    
    child_age = fields.Char(string='Age')
    child_gender = fields.Selection([('1', 'Male'),
                                     ('2', 'Female')], string='Gender', copy=False)
    
    emergancy_name = fields.Char(string='Emergency Contact Name')
    emergancy_contact_tele = fields.Char(string='Emergency Contact Telephone #')
    
    pick_up_people_ids = fields.One2many('pickup.people.details', 'camp_registration_id', 'Pick up People Details',help="The following people are permitted to pick up this child from camp")
    
    dietary_restrictions = fields.Selection([('1', 'Yes'),
                                       ('0', 'No')], string='Dietary restrictions', default='0')
    dietary_restriction_details = fields.Text(string='Dietary restrictions Details')
    child_medical_condition = fields.Text(string='Medical Conditions/Allergies')
    
    comments = fields.Text(string='Additional Information / Comments')
    
    child_medicare = fields.Char(string='Medicare')
    camp_registration_id = fields.Many2one('camp.registration',string='Camp Registration')

    name = fields.Char(string='Name', default="New")
    
#     mother_fname = fields.Char(string='Mother/Guardian First Name')
#     father_fname = fields.Char(string='Father/Guardian  first Name')
#     mother_fam_name = fields.Char(string='Mother/Guardian Family Name')
#     father_fam_name = fields.Char(string='Father/Guardian family Name')
#     street = fields.Char(string='street')
    
    
    apt = fields.Char(string='Apt')
    province = fields.Many2one('res.country.state',string='Province')
    
    pickup_contact_full_name = fields.Char(string='Full name of people who can pick-up my child/children after camp')

    #camp info
    language = fields.Selection([('1', 'English'),
                                       ('2', 'Français'),
                                       ('3', 'Bilingual')], string='Language')
    
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
    condition_one = fields.Boolean(string='I have read and agree to the terms &amp; conditions and waiver of liability. ')
    condition_two = fields.Boolean(string='I hereby grant permission to Everblast Backyard Camp to take photographs and video of my child to be used for promotional, instructional, educational or commercial purposes.')

    #terms and condition

    terms_condition = fields.Html(default= agreemnet_terms)
#     child_ids = fields.One2many('child.details', 'camp_registration_id', 'Child Details')
    # sale order
    sale_order_id = fields.Many2one('sale.order', string='Rental Quote')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active')], string='State')
    
#     camp_week_selection_ids = fields.One2many('camp.week.selection', 'camp_registration_id', 'Camp Weeks Selection')
    camp_date_selection_ids = fields.One2many('camp.date.selection', 'camp_registration_id', 'Camp Dates Selection')
    total_camp_days = fields.Float("Total Days", compute='_compute_total_days', store=True)


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

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'camp.registration') or 'New'
        # if vals['parent_name']:
            # partner_id=self.env['res.partner'].search([('name','=',vals['parent_name']),('phone','=',vals['tele_phone'])], limit=1)
            # camp_product = self.env['product.product'].search([('camp_registration_product', '=', '1')], limit=1)
            # if camp_product:
            #
                # total_camp_days = 0
                # if vals.get('camp_date_selection_ids'):
                    # for camp_date_selection_id in vals['camp_date_selection_ids']:
                        # if camp_date_selection_id[2]['slot'] == 'AM' or camp_date_selection_id[2]['slot'] == 'PM':
                           # total_camp_days += 0.5
                        # elif camp_date_selection_id[2]['slot'] == 'full':
                            # total_camp_days += 1
                            #
                # if partner_id:
                    # sale_order_obj = self.env['sale.order'].create({
                        # 'partner_id': partner_id.id,
                        # 'partner_invoice_id': partner_id.id,
                        # 'partner_shipping_id': partner_id.id,
                        # 'is_custom_rental_quote': True,
                        # 'order_line': [(0, 0, {
                            # 'name': 'Camp Day',
                            # 'product_id': camp_product.id,
                            # 'product_uom_qty': total_camp_days,
                            # # 'custom_rent_days': total_camp_days,
                            # 'product_uom': camp_product.uom_id.id,
                            # 'price_unit': camp_product.list_price,
                            #
                        # })],
                        # 'pricelist_id': self.env.ref('product.list0').id,
                        #
                    # })
                    # vals['sale_order_id'] = sale_order_obj.id
                # else :
                #
                    # new_partner_id = self.env['res.partner'].create({
                        # 'name': vals['parent_name'],
                        # 'is_company': True,
                        # 'email': vals.get('email'),
                        # 'phone': vals.get('tele_phone')
                    # })
                    #
                    # sale_order_obj =self.env['sale.order'].create({
                        # 'partner_id': new_partner_id.id,
                        # 'partner_invoice_id': new_partner_id.id,
                        # 'partner_shipping_id': new_partner_id.id,
                        # 'is_custom_rental_quote': True,
                        # 'order_line': [(0, 0, {
                            # 'name': 'Camp Day',
                            # 'product_id':camp_product.id,
                            # 'product_uom_qty': total_camp_days,
                            # # 'custom_rent_days': total_camp_days,
                            # 'product_uom': camp_product.uom_id.id,
                            # 'price_unit': camp_product.list_price,
                        # })],
                        # 'pricelist_id': self.env.ref('product.list0').id,
                        #
                     # })
                    # vals['sale_order_id'] = sale_order_obj.id
            # else :
                # return super(Campregistration, self).create(vals)

        return super(Campregistration, self).create(vals)

    def get_camp_vals(self):
        vals = {}
        if self.parent_name:
            vals = {
                'camp_registration_id': self.id,
                'camp_ref_code': self.ref_code,
                'child_name': self.child_name,
                'child_family_name': self.child_family_name,
                'child_dob': self.child_dob,
                'parent_name': self.parent_name,
                'parent_family_name': self.parent_family_name,
                'campreg_civic_number': self.civic_number,
                'campreg_city': self.city,
                'campreg_postal_code': self.postal_code,
                'campreg_email': self.email,
                'campreg_tele_phone': self.tele_phone,
                'child_age': self.child_age,
                'child_gender': self.child_gender,
                'emergancy_name': self.emergancy_name,
                'emergancy_contact_tele': self.emergancy_contact_tele,
                'dietary_restrictions': self.dietary_restrictions,
                'dietary_restriction_details': self.dietary_restriction_details,
                'child_medical_condition': self.child_medical_condition,
                'campreg_comments': self.comments,
                'is_camp_organizer': self.is_camp_organizer,
                'camp_organizer': self.camp_organizer,
                'camp_organizer_phone': self.camp_organizer_phone,
                'camp_organizer_email': self.camp_organizer_email,
                'camp_date_time': self.camp_date_time,
                'camp_host_name': self.camp_host_name,
                'camp_family_name': self.camp_family_name,
                'camp_email': self.camp_email,
                'camp_phone': self.camp_phone,
                'camp_street': self.camp_street,
                'camp_city': self.camp_city,
                'camp_province': self.camp_province,
                'camp_postal_code': self.camp_postal_code,
                'camp_location': self.camp_location,
                'camp_rain_plan': self.camp_rain_plan,
                'camp_first_date': self.camp_first_date,
                'is_more_camp_host': self.is_more_camp_host,
                'play_check': self.play_check,
                'camp_condition_one': self.condition_one,
                'camp_condition_two': self.condition_two,
                'camp_terms_condition': self.terms_condition,
                'pick_up_people_ids': [(6, 0, self.pick_up_people_ids.ids)],
                'camp_date_selection_ids': [(6, 0, self.camp_date_selection_ids.ids)],
            }
        return vals
    
    def create_rental_quote(self):
        if self.parent_name:
            p_name = self.parent_name
            if self.parent_family_name:
                p_name = self.parent_name+' '+self.parent_family_name
            partner_id = self.env['res.partner'].search([('name','=',p_name)], limit=1)
            camp_product = self.env['product.product'].search([('camp_registration_product', '=', '1')], limit=1)
            vals = self.get_camp_vals()
            if camp_product:
                if partner_id:
                    vals.update({
                        'partner_id': partner_id.id,
                        'partner_invoice_id': partner_id.id,
                        'partner_shipping_id': partner_id.id,
                        'is_custom_rental_quote': True,
                        'order_line': [(0, 0, {
                            'name': 'Camp Day',
                            'product_id': camp_product.id,
                            'product_uom_qty': self.total_camp_days,
                            # 'custom_rent_days': self.total_camp_days,
                            'product_uom': camp_product.uom_id.id,
                            'price_unit': camp_product.list_price,
                        })],
                        'pricelist_id': self.env.ref('product.list0').id,
                        })
                    sale_order_obj = self.env['sale.order'].create(vals)
                    self.sale_order_id = sale_order_obj.id
                else:
                    p_name = self.parent_name
                    if self.parent_family_name:
                        p_name = self.parent_name+' '+self.parent_family_name
                    new_partner_id = self.env['res.partner'].create({
                        'name': p_name,
                        'is_company': False,
                        'email': self.email,
                        'phone': self.tele_phone,
                        'street': self.civic_number,
                        'city': self.city,
                        'zip': self.postal_code
                    })
                    vals.update({
                        'partner_id': new_partner_id.id,
                        'partner_invoice_id': new_partner_id.id,
                        'partner_shipping_id': new_partner_id.id,
                        'is_custom_rental_quote': True,
                        'order_line': [(0, 0, {
                            'name': 'Camp Day',
                            'product_id':camp_product.id,
                            'product_uom_qty': self.total_camp_days,
                            # 'custom_rent_days': self.total_camp_days,
                            'product_uom': camp_product.uom_id.id,
                            'price_unit': camp_product.list_price,
                        })],
                        'pricelist_id': self.env.ref('product.list0').id,
                     })
                    sale_order_obj = self.env['sale.order'].create(vals)
                    self.sale_order_id = sale_order_obj.id
            else:
                raise UserError(_('Please add  product.'))

    def update_sale_camp_info(self):
        camp_objs = self.search([('sale_order_id','!=', False)])
        for camp_obj in camp_objs:
            vals = camp_obj.get_camp_vals()
            camp_obj.sale_order_id.write(vals)
            

class ChildDetails(models.Model):
    _name = "child.details"
    _description = "Child Details"
 
    child_name = fields.Char(string='Child First Name')
    child_fam_name = fields.Char(string='Family Name')
    child_age = fields.Char(string='Age')
    child_gender = fields.Selection([('1', 'Male'),
                                       ('2', 'Female')], string='Gender', copy=False)
    child_medical_condition = fields.Text(string='Medical Conditions/Allergies')
    child_medicare = fields.Char(string='Medicare')
    camp_registration_id = fields.Many2one('camp.registration',string='Camp Registration')


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    camp_registration_product = fields.Boolean( 'Camp Registration product', default=False)

