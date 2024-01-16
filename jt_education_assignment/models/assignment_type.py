from odoo import models, fields


class AssigmentType(models.Model):
	_name = 'assignment.type'
	_description = "Assignment Type"

	name = fields.Char(string="Name", required=True)
	code = fields.Char(string="Code")
	assign_type = fields.Selection([('sub', 'Subjective'),
									('attendance', 'Attendance')],
								   string='Type', default='sub')