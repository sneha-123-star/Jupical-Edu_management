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
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class StudentAssignment(models.Model):
    _name = "student.assignment"
    _inherit = "mail.thread"
    _description = "Assignment"

    name = fields.Char('Name')
    subject_id = fields.Many2one('student.subject', string='Subject')
    issued_date = fields.Datetime('Issued Date')
    assignment_type = fields.Many2one('assignment.type',string='Assignment Type')
    marks = fields.Float('Total Marks')
    description = fields.Text('Description')
    state = fields.Selection([
        ('draft', 'Draft'), ('publish', 'Published'),
        ('finish', 'Finished'), ('cancel', 'Cancel'),
    ], 'State', default='draft')
    submission_date = fields.Datetime('Submission Date')
    allocation_ids = fields.Many2many('res.partner', string='Allocated To',domain=[('is_student', '=', True)])
    assignment_submission = fields.One2many('student.assignment.submission','assignment_id', 'Submissions')
    faculty = fields.Many2one('res.partner', 'Faculty', domain=[('is_faculty', '=', True)])
    active = fields.Boolean(default=True)
    standard_id = fields.Many2one('student.standard',string="Standard")
    division_id = fields.Many2one('standard.division',string="Division")
    curr_year = fields.Many2one('year.year', string="Year")

    @api.constrains('issued_date', 'submission_date')
    def check_dates(self):
        for record in self:
            if record.issued_date > record.submission_date:
                raise ValidationError(_(
                    "Submission Date cannot be before Issue Date."))

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
