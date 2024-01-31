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
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from dateutil import relativedelta
from datetime import datetime, timedelta
from collections import OrderedDict
import calendar

class PrintAttendance(models.Model):
    _name = 'print.attendance'
    _description = 'Attendance Report'

    start_date = fields.Date(string='From', required=True)
    end_date = fields.Date(string='To', required=True)
    standard_id = fields.Many2one('student.standard', required=True)
    division_id = fields.Many2one('standard.division', required=True)
    student_id = fields.Many2one('res.partner', string="Students", domain=[('is_student','=', True)])
    date = fields.Date(string="Today's Date", default=fields.Date.today())
    attendance_line_ids = fields.One2many('attendance.line', 'date', string='Attendance Lines')
    faculty_id = fields.Many2one('res.partner',string="Faculties", domain=[('is_faculty', '=', True)], required=True)
    duration = fields.Selection([('daily','Daily'),('monthly','Monthly'),('custom','Custom Period')],'Summary')
    monthly = fields.Selection([('jan','January'),('feb','February'),('mar','March'),('apr','April'),('may','May'),('jun','June'),
              ('jul','July'),('aug','August'),('sep','September'),('oct','October'),('nov','November'),('dec','December')],'Month')
    

    def generate_attendance_report(self):
        self.ensure_one()    
        return self.env.ref('jt_education_attendance.action_attendance_report').report_action(self.id)



    def ger_report_data(self):
        stud_ids = []
    
        students = self.env['res.partner'].search([('is_student', '=', True), ('standard','=',self.standard_id.id), ('div','=',self.division_id.id),('id', 'not in', stud_ids)])
        faculties = self.env['res.partner'].search([('is_faculty','=', True)])
        print('fac!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',faculties)
        attendance_lines = self.env['attendance.line'].search([('student_id','in',students.ids),('attendance_id.date','>=',self.start_date),('attendance_id.date','<',self.end_date)])
        print("stu records!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",attendance_lines)

        r = relativedelta.relativedelta( self.end_date,self.start_date)
        month_name_list = OrderedDict(((self.start_date + timedelta(_)).strftime(r"%B-%Y"), None) for _ in range((self.end_date - self.start_date).days)).keys()
        number_days =[]
        weekday_names= False
        for m_data in list(month_name_list):
            month_name = m_data.split('-')
            month_number = list(calendar.month_name).index(month_name[0])
            # print('month_name[1]--->>>>>>>>',calendar.monthrange(month_name[1], month_number)[1])
            n_days = calendar.monthrange(int(month_name[1]),int( month_number))[1]
            weekday_names = [calendar.day_name[(calendar.weekday(int(month_name[1]),int(month_number), day) + 1) % 7] for day in range(1, n_days + 1)]
            number_days.append((n_days,weekday_names))
        months_difference = (r.years * 12) + r.months
        data = {'attendance_lines':attendance_lines,
        'months_difference':months_difference,
        'month_name':list(month_name_list),
        'number_days':number_days,
        'student_id':stud_ids,  
        'students': students,
        'faculties':faculties,
        'month_number' : month_number
        }
        return data