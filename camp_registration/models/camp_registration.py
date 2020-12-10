from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError

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

    name = fields.Char(string='Name', default="New")
    ref_code = fields.Char(string='Reference Code')
    mother_fname = fields.Char(string='Mother/Guardian First Name')
    father_fname = fields.Char(string='Father/Guardian  first Name')
    mother_fam_name = fields.Char(string='Mother/Guardian Family Name')
    father_fam_name = fields.Char(string='Father/Guardian family Name')
    street = fields.Char(string='street')
    city = fields.Char(string='City')
    civic_number = fields.Char(string='Civic Number')
    apt = fields.Char(string='Apt')
    province = fields.Many2one('res.country.state',string='Province')
    postal_code = fields.Char(string='Postal code')
    email = fields.Char(string='Email address')
    tele_phone = fields.Char(string="Telephone")
    emergancy_name = fields.Char(string='Emergency Contact Name')
    emergancy_contact_tele = fields.Char(string='Emergency Contact Tel')
    pickup_contact_full_name = fields.Char(string='Full name of people who can pick-up my child/children after camp')

    #camp info
    language = fields.Selection([('1', 'English'),
                                       ('2', 'Français'),
                                       ('3', 'Bilingual')], string='Language')
    camp_date_time = fields.Datetime(string='Date and Time')
    camp_location = fields.Char(string='Host Name/Park')
    camp_civic = fields.Char(string='Civic')
    camp_street = fields.Char(string='Street')
    camp_city = fields.Char(string='City')
    camp_province = fields.Many2one('res.country.state',string='Province')
    camp_postal_code = fields.Char(string='Postal Code')
    play_check = fields.Boolean(string='Are your kids allowed to play at the park? y/n')

    #marketting
    condition_one = fields.Boolean(string='I accept to receive email communications, including promotional material from Everblast. ')
    condition_two = fields.Boolean(string='I hereby grant permission to Everblast Backyard Camp to take photographs and video of my child/children  to be used for promotional, instructional, educational or commercial purposes.')

    #terms and condition

    terms_condition = fields.Html(default= agreemnet_terms)
    child_ids = fields.One2many('child.details', 'camp_registration_id', 'Child Details')
    # sale order
    sale_order_id = fields.Many2one('sale.order', string='Sale order')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active')], string='State')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'camp.registration') or 'New'

        if vals['mother_fname']:
            partner_id=self.env['res.partner'].search([('name','=',vals['mother_fname']),('phone','=',vals['tele_phone'])])
            camp_product = self.env['product.product'].search([('camp_registration_product', '=', '1')], limit=1)
            if camp_product:
                if partner_id:
                    sale_order_obj = self.env['sale.order'].create({
                        'partner_id': partner_id.id,
                        'partner_invoice_id': partner_id.id,
                        'partner_shipping_id': partner_id.id,
                        'order_line': [(0, 0, {
                            'name': 'test',
                            'product_id': camp_product.id,
                            'product_uom_qty': len(vals['child_ids']),
                            'product_uom': camp_product.uom_id.id,
                            'price_unit': camp_product.list_price,
                        })],
                        'pricelist_id': self.env.ref('product.list0').id,

                    })
                    vals['sale_order_id'] = sale_order_obj.id
                else :

                    new_partner_id = self.env['res.partner'].create({
                        'name': vals['mother_fname'],
                        'is_company': True,
                        'email': vals.get('email'),
                        'phone': vals.get('tele_phone')
                    })

                    sale_order_obj =self.env['sale.order'].create({
                        'partner_id': new_partner_id.id,
                        'partner_invoice_id': new_partner_id.id,
                        'partner_shipping_id': new_partner_id.id,
                        'order_line': [(0, 0, {
                            'name': 'test',
                            'product_id':camp_product.id,
                            'product_uom_qty': len(vals['child_ids']),
                            'product_uom': camp_product.uom_id.id,
                            'price_unit': camp_product.list_price,
                        })],
                        'pricelist_id': self.env.ref('product.list0').id,

                     })
                    vals['sale_order_id'] = sale_order_obj.id
            else :
                return super(Campregistration, self).create(vals)


        return super(Campregistration, self).create(vals)

    def create_sale_order(self):
        if self.mother_fname:
            partner_id = self.env['res.partner'].search([('name','=',self.mother_fname)])
            camp_product = self.env['product.product'].search([('camp_registration_product', '=', '1')], limit=1)
            if camp_product:
                if partner_id:
                    sale_order_obj = self.env['sale.order'].create({
                        'partner_id': partner_id.id,
                        'partner_invoice_id': partner_id.id,
                        'partner_shipping_id': partner_id.id,
                        'order_line': [(0, 0, {
                            'name': 'test',
                            'product_id': camp_product.id,
                            'product_uom_qty': len(self.child_ids),
                            'product_uom': camp_product.uom_id.id,
                            'price_unit': camp_product.list_price,
                        })],
                        'pricelist_id': self.env.ref('product.list0').id,

                    })
                    self.sale_order_id = sale_order_obj.id
                else :

                    new_partner_id = self.env['res.partner'].create({
                        'name': self.mother_fname,
                        'is_company': False,
                        'email': self.email,
                        'phone': self.tele_phone
                    })

                    sale_order_obj =self.env['sale.order'].create({
                        'partner_id': new_partner_id.id,
                        'partner_invoice_id': new_partner_id.id,
                        'partner_shipping_id': new_partner_id.id,
                        'order_line': [(0, 0, {
                            'name': 'test',
                            'product_id':camp_product.id,
                            'product_uom_qty': len(self.child_ids),
                            'product_uom': camp_product.uom_id.id,
                            'price_unit': camp_product.list_price,
                        })],
                        'pricelist_id': self.env.ref('product.list0').id,

                     })
                    self.sale_order_id = sale_order_obj.id
            else:
                raise UserError(_('Please add  product.'))

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

