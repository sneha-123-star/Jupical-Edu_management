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
from odoo import models, fields, api, exceptions, _


class SubjectLine(models.Model):
    _name = 'subject.line'
    _description = 'Subject Line'

    subject_id = fields.Many2one(
        'student.subject', string='Subject', required=True, help="Select Subjects")
    date = fields.Date(string='Date', required=True)
    day = fields.Selection([('sunday', 'Sunday'), ('monday', 'Monday'),
                              ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'),('thursday', 'Thursday'),
                              ('friday', 'Friday'), ('saturday', 'Saturday')], default='monday')
    time_from = fields.Float(string='Time From', required=True, help="Start time")
    time_to = fields.Float(string='Time To', required=True, help="Finish time")
    mark = fields.Integer(string='Mark',help="Total Marks of Subject")
    exam_id = fields.Many2one('student.exam', string='Exam')

class StudentSubject(models.Model):
    _name = 'student.subject'
    _description = 'Student Subject'
    _sql_constraints = [
        ('code', 'unique(code)', "Another Subject already exists with this code!"), ]

    name = fields.Char(string='Name', required=True, help="Name of the Subject")
    code = fields.Char(string="Code", help="Enter the Subject Code")
    subject_category_ids = fields.Many2many('subject.category', 'subject_for_id', string="Subject Categories")

    def name_get(self):
        res = []
        for rec in self:
            name = rec.name or ''  
            res.append((rec.id, '%s - %s' % (rec.code or '', name)))
        return res

   

class StudentExam(models.Model):
    _name = 'student.exam'
    _description = 'Generate Student Exams'

    # default method to have code and name displayed together.
    def name_get(self):
        res = []
        for rec in self:

            res.append((rec.id, '%s - %s(%s-%s)' % (rec.name,
                                                 rec.start_date, rec.standard.name,rec.division.name)))
        return res

    @api.constrains('start_date', 'end_date')
    def check_dates(self):
        for rec in self:
            if rec.start_date > rec.end_date:
                raise ValidationError("Start date must be Greater to end date")

    student_ids = fields.Many2many(
        'res.partner', domain=[('is_student', '=', True)])
    name = fields.Char(string='Name', required=True)
    start_date = fields.Date('Start Date', required=True)
    end_date = fields.Date('End Date', required=True)
    subject_line = fields.One2many(
        'subject.line', 'exam_id', string='Subjects')
    standard = fields.Many2one(
        'student.standard', string="Standard", required=True)
    division = fields.Many2one(
        'standard.division', string="Division", required=True)
    curr_year = fields.Many2one('year.year', string='Current Year', required=True)
    state = fields.Selection([('draft', 'Draft'), ('ongoing', 'On Going'),
                              ('close', 'Closed'), ('cancel', 'Canceled')], default='draft')

    def close_exam(self):
        self.state = 'close'

    def cancel_exam(self):
        self.state = 'cancel'

    def ongoing_exam(self):
        self.state = 'ongoing'
