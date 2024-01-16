from odoo import models, fields, api
from odoo.exceptions import ValidationError

class PrintAttendance(models.Model):
    _name = 'print.attendance'
    _description = 'Attendance Report'

    start_date = fields.Date(string='From', required=True)
    end_date = fields.Date(string='To', required=True)


    def generate_attendance_report(self):
        self.ensure_one()        
        return self.env.ref('jt_education_attendance.action_attendance_report').report_action(self)