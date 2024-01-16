from odoo import fields, models, api, exceptions, _

class Attendance(models.Model):
    _name = 'attendance.attendance'

    faculty_id = fields.Many2one('res.partner', domain=[('is_faculty', '=', True)], required=True)
    standard_id = fields.Many2one('student.standard', required=True)
    division_id = fields.Many2one('standard.division', required=True)
    subject_id = fields.Many2many('student.subject', string="Subjects", required=True)
    date = fields.Date(string="Today's Date", default=fields.Date.today())
    attendance_ids = fields.One2many('attendance.line', 'attendance_id', string="Attendance Line")
    student_id = fields.Many2one('res.partner', string="Students", domain=[('is_student', '=', True)])


    _sql_constraints = [
        ('code_faculty_id_uniq', 'unique(subject_id,standard_id,date)', "Attendance for this faculty and standard already exists!")
    ]   

    def select_all_line(self):
        for line in self.attendance_ids:
            line.selected = True

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s - %s(%s)' % (rec.faculty_id.name, rec.standard_id.name, rec.division_id.name)))
        return res

class AttendanceLine(models.Model):
    _name = 'attendance.line'

    attendance_id = fields.Many2one('attendance.attendance', string="Attendance")
    name = fields.Char(related='student_id.name', string="Name", help="Student List is displayed based on standard and division.")
    student_id = fields.Many2one('res.partner', string="Students", domain=[('is_student', '=', True)])
    roll_no = fields.Integer(related='student_id.roll_no', string="Roll Number")
    present = fields.Boolean(string="Present")
    absence_reason = fields.Boolean(string="Absence with Reason")
    absence_noreason = fields.Boolean(string="Absence with no Reason")
    late = fields.Boolean(string="Late")
    withdraw = fields.Boolean(string="Withdraw")

    standard_id = fields.Many2one('student.standard', required=True,related="attendance_id.standard_id")
    division_id = fields.Many2one('standard.division', required=True,related="attendance_id.division_id")
    selected = fields.Boolean("Select")



    @api.onchange('student_id')
    def onchange_student_id(self):        
        if self.student_id:
            existing_record = self.search([
                ('student_id', '=', self.student_id.id)])
            print("exists-----",existing_record)
            if existing_record:
                raise exceptions.ValidationError(_('Attendance for this student  already exists!'))

	
