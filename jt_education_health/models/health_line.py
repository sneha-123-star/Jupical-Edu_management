from odoo import models, fields


class JtHealthLine(models.Model):
    _name = 'health.health.line'
    _description = 'Health line'

    health_id = fields.Many2one('health.health', 'Health')
    date = fields.Date('Date', default=lambda self: fields.Date.today())
    name = fields.Text('Checkup Detail', required=True)
    recommendation = fields.Text('Checkup Recommendation')
