from odoo import models, fields

class Product(models.Model):
    _inherit = 'product.product'


    e_ticket = fields.Boolean(string="E-ticket")
