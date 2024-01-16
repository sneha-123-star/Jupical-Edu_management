from odoo import models, fields


class AssignmentStudent(models.Model):
    _inherit = "res.partner"
    _description = "Assignment Student Class"

    allocation_ids = fields.Many2many('student.assignment', string='Assignment(s)')
    assignment_count = fields.Integer(compute='compute_count_assignment')

    def get_assignment(self):
        action = self.env.ref('jt_education_assignment.'
                              'action_student_assignment').read()[0]
        action['domain'] = [('allocation_ids', 'in', self.ids), ('state', '=', 'publish')]
        return action

    def compute_count_assignment(self):
        for record in self:
            record.assignment_count = self.env['student.assignment'].search_count(
                [('allocation_ids', '=', self.id), ('state', '=', 'publish')])