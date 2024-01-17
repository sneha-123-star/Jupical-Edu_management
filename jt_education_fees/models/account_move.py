# -*- coding: utf-8 -*-
##############################################################################
#
#    Jupical Technologies Pvt. Ltd.
#    Copyright (C) 2018-TODAY Jupical Technologies(<http://www.jupical.com>).
#    Author: Jupical Technologies Pvt. Ltd.(<http://www.jupical.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
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