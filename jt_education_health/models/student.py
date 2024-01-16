from odoo import models, fields

class JtStudent(models.Model):

    _inherit = 'res.partner'

    health_lines = fields.One2many('health.health', 'student_id', 'Health Detail')
