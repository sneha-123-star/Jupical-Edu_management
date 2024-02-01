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
from odoo import models, fields, api,_
from odoo.exceptions import ValidationError


class ExamResult(models.Model):
    _name = 'student.result'
    _description = 'Generate Student Result'

    # default method to have code and name displayed together.
    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s-%s (%s)' % (rec.student_id.stud_id,
                                                rec.student_id.name, rec.exam_id.name)))
        return res

    student_id = fields.Many2one('res.partner', string='Student', domain=[
                                 ('is_student', '=', True)])
    standard = fields.Many2one(related="student_id.standard")
    division = fields.Many2one(related="student_id.div")
    academic_year = fields.Many2one(related='student_id.curr_year', store=True)
    exam_id = fields.Many2one('student.exam', string='Exam')
    subject_line = fields.One2many(
        'result.subject.line', 'result_id', string='Subjects')
    total_pass_mark = fields.Float(
        string='Total Passing Marks', store=True, readonly=True, compute='_total_marks_all')
    total_mark = fields.Float(
        string='Total Marks', store=True, readonly=True, compute='_total_marks_all')
    total_mark_scored = fields.Float(
        string='Total Marks Scored', store=True, readonly=True, compute='_total_marks_all')
    pass_fail_full = fields.Boolean(
        string='Pass/Fail', store=True, readonly=True, compute='_total_marks_all')
    percentage = fields.Float('Percentage',compute='_compute_percentage') 
    input_line = fields.Char("Note")
    faculty_id = fields.Many2one('res.partner', domain=[('is_faculty', '=', True)], required=True)
    parent_id = fields.Many2one('res.partner', domain=[('is_parent', '=', True)], required=True)
    english_id = fields.Many2one('res.partner', domain=[('is_faculty', '=', True)], string="English Teacher")
    chineses_id = fields.Many2one('res.partner', domain=[('is_faculty', '=', True)], string="Chinese Teacher")
    lao_id = fields.Many2one('res.partner', domain=[('is_faculty', '=', True)], string="Lao Teacher")



    @api.onchange('exam_id')
    def _onchange_exam_id(self):
        subject_line_data = [(5, 0, 0)]
        for subject_line in self.exam_id.subject_line:
            line = (0, 0, {
            'subject_id': subject_line.subject_id.id,
            'subject_category_ids': [(6, 0, subject_line.subject_id.subject_category_ids.ids)],
            'exam_id':self.exam_id.id,
            'student_id':self.student_id.id,
            })
            subject_line_data.append(line)
        self.subject_line = subject_line_data

    @api.depends('subject_line.mark_scored')
    def _total_marks_all(self):
        for results in self:
            total_pass_mark = 0
            total_mark = 0
            total_mark_scored = 0
            pass_fail_full = True
            for subjects in results.subject_line:
                total_pass_mark += subjects.pass_mark
                total_mark += subjects.mark
                total_mark_scored += subjects.mark_scored
                if not subjects.pass_or_fail:
                    pass_fail_full = False
            results.total_pass_mark = total_pass_mark
            results.total_mark = total_mark
            results.total_mark_scored = total_mark_scored
            results.pass_fail_full = pass_fail_full

    def _compute_percentage(self):
        for record in self:
        # Percentage = (Value ⁄ Total Value) × 100
            record.percentage = (record.total_mark_scored/record.total_mark)*100 if record.total_mark != 0 else 0
        # print("percentage..........",self.percentage)

    def get_gread_records(self):
        return self.env['result.grade'].search([])

    

class ResultSubjectLine(models.Model):
    _name = 'result.subject.line'
    _description = "Result Subject Line"
    
    mark = fields.Float('Marks',compute="_compute_category_marks")
    pass_mark = fields.Float('Passing Marks',compute="_compute_category_marks")
    mark_scored = fields.Float('Marks Scored',compute="_compute_category_marks")
    pass_or_fail = fields.Boolean('Pass/Fail',compute="_compute_category_marks")
    result_id = fields.Many2one('student.result', string='Result Id')
    percentage = fields.Float('Percentage',compute="_compute_category_marks")

    exam_id = fields.Many2one('student.exam', string='Exam')
    grade_id = fields.Many2one('result.grade', string="Grade")
    standard = fields.Many2one(related="student_id.standard")
    division = fields.Many2one(related="student_id.div")
    student_id = fields.Many2one('res.partner', string='Student',related="result_id.student_id",store=True)
    subject_category_ids = fields.One2many("subject.category", 'subject_line_id', string="Subject categories")
    academic_year = fields.Many2one(related='student_id.curr_year', store=True)

    _sql_constraints = [
        ('unique_subject_result', 'unique(subject_id, result_id)', 'Subject in result must be unique!'),
    ]

    exam_id = fields.Many2one('student.exam', string='Exam', store=True)
    grade_id = fields.Many2one('result.grade',string="Grade",compute="get_grade_id")
    standard = fields.Many2one(related="student_id.standard")
    division = fields.Many2one(related="student_id.div")
    # student_id = fields.Many2one('res.partner', string='Student', domain=[
    #                              ('is_student', '=', True)],store=True)
    subject_category_ids = fields.One2many("subject.category",'subject_line_id',string="Subject categories")
    academic_year = fields.Many2one(related='student_id.curr_year', store=True)
    subject_id = fields.Many2one('student.subject', string='Subject',required=True,)

    @api.depends('percentage')
    def get_grade_id(self):
        grade_ids = self.env['result.grade'].search([])
        for line in self:
            for grade in grade_ids:
                grade_data = grade.mark_range.split('-')
                if int(line.percentage) in range(int(grade_data[0]),int(grade_data[1])):
                    line.grade_id = grade.id
                    break;
                else:
                    line.grade_id =False



    @api.depends('subject_id','subject_category_ids','pass_mark','mark_scored','mark')
    def _compute_category_marks(self):
        for total_category in self:
            cat_mark = 0
            cat_pass_mark = 0
            cat_mark_scored = 0
            for cat_sub in total_category.subject_category_ids:
                cat_mark += cat_sub.mark
                cat_pass_mark += cat_sub.pass_mark
                cat_mark_scored += cat_sub.actual_mark
            total_category.mark =  cat_mark
            total_category.pass_mark = cat_pass_mark
            total_category.mark_scored = cat_mark_scored
            total_category.percentage = cat_mark_scored *cat_mark /100
            if total_category.percentage >= 40.00:
                total_category.pass_or_fail = True
            else:
                total_category.pass_or_fail = False




    @api.depends('subject_id')
    def subject_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s - %s' % (rec.subject_id)))
        return res
    


    @api.onchange('subject_id')
    def onchange_subject_id(self):
               
        self.subject_category_ids =  [(6, 0, self.subject_id.subject_category_ids.ids)]


class Grade(models.Model):
    _name = 'result.grade'
    _description = 'Result Grade'

    name = fields.Char('Grade')
    mark_range = fields.Char('Mark Range')

class SubjectCategory(models.Model):
    _name = 'subject.category'
    _description = 'Subject Category'

    name = fields.Char('Name')
    mark = fields.Float('Marks')
    actual_mark = fields.Float('Actual Marks')
    subject_for_id = fields.Many2one('student.subject',string="standard")
    subject_line_id = fields.Many2one('result.subject.line',string="subject line")
    pass_mark = fields.Float('Passing Marks')





