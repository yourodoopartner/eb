from odoo import api, fields, models, _


class ProductCategory(models.Model):
    _inherit = "product.category"

    is_staff = fields.Boolean(string='Staff')
