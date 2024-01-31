from odoo import fields,models

class StudentProvince(models.Model):
    _name = 'province.province'
    _description = 'Student Province'

    is_country = fields.Boolean('Country')
    name = fields.Char(string='Name')
    country = fields.Many2one('res.country',string="Country")

