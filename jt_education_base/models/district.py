from odoo import fields,models

class StudentDistrict(models.Model):
    _name = 'district.district'
    _description = 'Student District'

    name = fields.Char(string='Name', required=True)
    state = fields.Many2one('res.country.state',string="State")
    country = fields.Many2one('res.country',string="Country",related="state.country_id")
