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


class StudentAssignmentSubmission(models.Model):
	_name = "student.assignment.submission"
	_inherit = "mail.thread"
	_description = "Assignment Submission"

	assignment_id = fields.Many2one(
		'student.assignment',string='Assignment',required=True, help="Enter Students to see assignments assigned to them.")
	student_id = fields.Many2many(
		'res.partner', string='Students', domain=[('is_student', '=', True)])
	description = fields.Text('Description')
	state = fields.Selection([
		('draft', 'Draft'), ('submit', 'Submitted'), ('reject', 'Rejected'),
		('change', 'Change Req.'), ('accept', 'Accepted')], basestring='State',
		default='draft')
	submission_date = fields.Datetime(
		'Submission Date', readonly=True,
		default=lambda self: fields.Datetime.now())
	marks = fields.Float(related='assignment_id.marks')
	marks_scored = fields.Float('Scored Marks')
	note = fields.Text('Note')
	active = fields.Boolean(default=True)
	standard_id = fields.Many2one('student.standard',string="Standard",required=True)
	division_id = fields.Many2one('standard.division',string="Division",required=True)
	curr_year = fields.Many2one('year.year', string="Year")
	attachment = fields.Many2many('ir.attachment', 'attach_rel', 'doc_id','attach_id3',string="Attachment",help='You can attach the copy of your document', copy=False)

	def name_get(self):
		res = []
		for rec in self:
			res.append((rec.id, '%s(%s-%s)' % (rec.assignment_id.name, rec.standard_id.name,rec.division_id.name)))
		return res

	def act_draft(self):
		result = self.state = 'draft'
		return result and result or False

	def act_submit(self):
		result = self.state = 'submit'
		return result and result or False

	def act_accept(self):
		result = self.state = 'accept'
		return result and result or False

	def act_change_req(self):
		result = self.state = 'change'
		return result and result or False

	def act_reject(self):
		result = self.state = 'reject'
		return result and result or False

class AttachmentSubmission(models.Model):

	_inherit = 'ir.attachment'

	attach_rel = fields.Many2many('res.partner', 'attachment', 'attachment_id3', 'document_id',string="Attachment", invisible=1)
