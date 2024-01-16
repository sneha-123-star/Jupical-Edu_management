# -*- coding: utf-8 -*-
##############################################################################
#
#    AtharvERP Business Solutions
#    Copyright (C) 2020-TODAY AtharvERP Business Solutions(<http://www.atharverp.com>).
#    Author: AtharvERP Business Solutions(<http://www.atharverp.com>)
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
from odoo import models, fields

class StudentInformation(models.Model):

    _inherit = 'res.partner'
    _description = 'Student Information'

    rec_count = fields.Integer(string="Count",compute='get_records_count')
    book_id = fields.Many2one('issue.books', string="Issued Books")

    def action_view_issued_books(self):
        return{
            'name' : 'Books Issued',
            'type' : 'ir.actions.act_window',
            'view_mode' : 'tree,form,kanban',
            'res_model' : 'issue.books',
            'target' : 'current',
            'domain': [('student_id', '=', self.id), ('state', '=', 'issued')],
            'context': {'default_student_id': self.id},
        }   

    def get_records_count(self):
        count = self.env['issue.books'].search_count([('student_id', '=', self.id), ('state', '=', 'issued')])
        self.rec_count = count  
