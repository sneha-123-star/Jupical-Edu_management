from odoo import api, fields, models,_

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    fees_id = fields.Many2one('fees.fees',string="Fees Ref")

    def _create_invoices(self, grouped=False, final=False, date=None):
        res = super()._create_invoices(grouped=grouped, final=final, date=date)
        for sale in self:
            res.update({'fees_id':sale.fees_id and sale.fees_id.id or False})
            
            fees = self.env['fees.fees'].search([('id','=',sale.fees_id.id)],limit=1)
            fees.update({'state':'invoice','payment_state':'not_paid'})
        return res