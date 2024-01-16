from odoo import fields,models

class StudentVillage(models.Model):
    _name = 'village.village'
    _description = 'Student Village'

    name = fields.Char(string='Name')
    dis_id = fields.Many2one('district.district',string="District")
    state = fields.Many2one('res.country.state',string="State" ,related="dis_id.state")
    country = fields.Many2one('res.country',string="Country",related="dis_id.country")
