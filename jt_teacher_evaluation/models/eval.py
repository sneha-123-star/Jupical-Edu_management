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
from odoo import fields, models,_,api
from datetime import datetime,date

class Evaluation(models.Model):

    _name = 'eval.profile'

    name = fields.Char('Name' ,required=True)
    teacher_id = fields.Many2one('res.partner', string='Teacher',domain=[('is_faculty', '=', True)])
    date = fields.Date(string="Evaluation Date",default=fields.Date.today())
    user_type = fields.Selection([('student', 'Student'),('teacher', 'Teacher'),('parent', 'Parent')],default='teacher')
    user_id = fields.Many2one('res.users', 'User')
    state = fields.Selection([
        ('draft', 'Draft'), ('publish', 'In Progress'),
        ('finish', 'Finished'), ('cancel', 'Cancel'),
    ], 'State', default='draft')
    tab_ids = fields.One2many('eval.tab','tab_id',string="Table Line")
    student_id = fields.Many2one('res.partner', string='Student',domain=[('is_student', '=', True)])
    parent_id = fields.Many2one('res.partner', string='Parent',domain=[('is_parent', '=', True)])
    total = fields.Float("Total",compute="_compute_total_eval")

    @api.depends('tab_ids')
    def _compute_total_eval(self):
        for question in self.tab_ids:
            self.total += question.rating_id.rate

    def act_publish(self):
        result = self.state = 'publish'
        return result and result or False

    def act_finish(self):
        result = self.state = 'finish'
        return result and result or False

    def act_cancel(self):
        self.state = 'cancel'

    def act_set_to_draft(self):
        self.state = 'draft'

class Tabs(models.Model):

    _name = 'eval.tab'

    tab_id = fields.Many2one('eval.profile',string="General")
    question_id = fields.Many2one('eval.detail',string="Questions")
    rating_id = fields.Many2one("rating.remarks",string="Ratings")
    remarks = fields.Selection([('poor','Poor'),('average','Average'),('good','Good'),('very_good','Very Good'),('excellent','Excellent')],string="Comments",related="rating_id.remarks")
