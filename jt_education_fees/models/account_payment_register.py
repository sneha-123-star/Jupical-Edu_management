from odoo import api, fields, models, _
from datetime import datetime


class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    def action_create_payments(self):
        res = super(AccountPaymentRegister, self).action_create_payments()
        active_ids = self._context.get('active_ids')
        active_model = self.env.context.get('active_model')
        record =  self.env[active_model].browse(active_ids)
        
        if record.payment_state == 'paid':
        	fees = self.env['fees.fees'].sudo().search([('id','=',record.fees_id.id)],limit=1)
        	fees.update({'inv_ref':record.name,'paid_on':datetime.now(),'state':'paid','payment_state':'paid'})
        return res
