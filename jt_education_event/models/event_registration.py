from odoo import models, fields


class EventRegistration(models.Model):

    _inherit = 'event.registration'

    partner_id = fields.Many2one(
        'res.partner', string='Contact',
        states={'done': [('readonly', True)]}, domain=[('is_student', '=', True)])
