from odoo import models, fields

class JtFaculty(models.Model):

    _inherit = 'res.partner'

    health_faculty_lines = fields.One2many(
        'health.health', 'faculty_id', 'Health Detail')
