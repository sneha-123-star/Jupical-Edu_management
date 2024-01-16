from odoo import api, fields, models,_
from datetime import datetime

class AccountMove(models.Model):
    _inherit = 'account.move'

    fees_id = fields.Many2one('fees.fees',string="Fees Ref")
    standard = fields.Many2one(related='fees_id.standard', string="Standard")
    division = fields.Many2one(related='fees_id.division', string="Division")
    year = fields.Many2one(related='fees_id.year', string="Year")
    month = fields.Selection(related='fees_id.month', string="month")

    # def write(self, vals):
    #     res = super().write(vals)
    #     if self.state == 'posted':
    #         fees = self.env['fees.fees'].sudo().search([('id','=',self.fees_id.id)],limit=1)
    #         fees.update({'inv_ref':self.name,'paid_on':datetime.now(),'state':'paid'})
    #     return res