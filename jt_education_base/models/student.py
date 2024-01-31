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
from odoo import models, fields, api,exceptions, _
from datetime import datetime,date

# student information


class ResPartner(models.Model):

    _inherit = 'res.partner'
    _description = 'Student Information'
    _rec_name = 'stud_id'

    def name_get(self):
        res = []
        for rec in self:
            if rec.stud_id and rec.name:
                res.append((rec.id, '%s - %s' % (rec.stud_id, rec.name)))
            else:
                res.append((rec.id, '%s' % (rec.name)))
        return res

    # def get_year(self):
    #     return str(datetime.now().year)

    # Basic student detail
    is_student = fields.Boolean('Student')
    standard = fields.Many2one('student.standard', 'Standard' , required=True, help="Add Standard of student")
    div = fields.Many2one('standard.division', required=True, help="Add Division of student")
    curr_year = fields.Many2one('year.year', 'Current Year' ,required=True, help="Add current year of student")
                                                    # ,default=get_year 
    stud_id = fields.Char('Student ID' ,copy=False, help="Student ID")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')] ,default='male' ,required=True)
    working_days = fields.Char('Number of Working Days', size=3, help="Total Number of Working Days")
    working_days_present = fields.Char('Number of Working Days Present', size=3, help="Total Number of days present")
    lc_apply_date = fields.Date('Application Date of Leaving Certificate', help="Application Date of Leaving Certificate")
    lc_issue_date = fields.Date('Issue Date of Leaving Certificate', help="Issue Date of Leaving Certificate")
    detension = fields.Char('No. of Time Student is Detained', help="Number of Time Student is Detained")
    promotion = fields.Selection(string='Qualified for Promoting to Next Class',
        selection=[('yes', 'Yes'), ('no','No')])

    # Personal information
    roll_no = fields.Integer('Roll Number', copy=False , help="Roll Number")
    gr_no = fields.Char("GR Number", required=True , help="General Registration Number of student")
    father_name = fields.Char('Father Name', required=True)
    surname = fields.Char('Surname', required=True)
    # nickname = fields.Char('Nickname')
    mother_name = fields.Char('Mother Name')
    nationality = fields.Char('Nationality')
    mother_tonque = fields.Char('Mother Tongue')
    religion = fields.Char('Religion')
    caste = fields.Char('Caste')
    subcaste = fields.Char('SubCaste')
    birthPlace = fields.Char('Place of Birth')
    village = fields.Many2one('village.village',"village")
    district_id = fields.Many2one('district.district','District',related="village.dis_id")
    state1 = fields.Many2one('res.country.state', 'State',related="district_id.state")
    country1 = fields.Many2one('res.country', 'Country',related="district_id.country")
    
    birthdate = fields.Date('Date of Birth')
    lastschool = fields.Char('Last School Attended', help="Name of last school attended")
    last_std = fields.Char('Last Standard')
    date_admission = fields.Date('Date of admission in this school', help="Enter Date of admission in this school")
    adm_standard = fields.Many2one('student.standard', 'Admission Standard', help="Enter Standard in which student got admission in this school")
    
    progress = fields.Char('Progress')
    conduct = fields.Char('Conduct')
    howknow_id = fields.Many2one('how.know', 'How Student Know Our School')
    emergency_contact = fields.Char('Emergency Contact')
    leave_date = fields.Date('Date of Leaving School', help="Date of Leaving this school")
    std_studying = fields.Char('Studying in Standard', help="Studying in Current Standard")
    studying_since = fields.Char('Studying Since',help="Studying Since in this school")
    reason_for_leave = fields.Text('Reason for Leaving school')
    remarks = fields.Text('Remarks')
    # company_type = fields.Selection(
    #     string='Company Type',
    #     selection=[('student', 'Student'), ('person',
    #                                         'Individual'), ('company', 'Company')],
    #     compute='_compute_company_type', inverse='_write_company_type')
    signature = fields.Binary("Signature")
    parentsid = fields.Many2one('res.partner',string="Parents",domain=[('is_parent', '=', True)])
    age = fields.Integer("Age",store=True)
    detailed_age = fields.Char("Detailed Age",store=True)


    def get_days_in_month(self,month, year):
        if month == 2:  
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): 
                return 29 
            else:
                return 28
        elif month in [4, 6, 9, 11]:   
            return 30
        else:
            return 31

    @api.onchange('birthdate')
    def onchange_birthdate(self):
        if self.birthdate:
            today = date.today()
            self.age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
            years = today.year - self.birthdate.year
            months = today.month - self.birthdate.month
            days = today.day - self.birthdate.day

            # Adjust for negative differences
            if days < 0:
                months -= 1
                days += self.get_days_in_month(self.birthdate.month, self.birthdate.year)
            if months < 0:
                years -= 1
                months += 12

            self.detailed_age = str(years)+"  Years  "+str(months)+"  Months  "+str(days)+"  Days  "


    @api.constrains('birthdate')
    def validation_constraints(self):
        today=fields.Date.today()
        for rec in self:

            if rec.birthdate and rec.birthdate >=today:
                raise exceptions.ValidationError(_('Invalid date of birth ..please enter correct date'))

    @api.model
    def create(self, vals):
        res = super(ResPartner, self).create(vals)
        if res.company_type == 'student':
            res.stud_id = self.env['ir.sequence'].next_by_code(
                'studentinformation.seq')
        return res

    def get_roll_no(self):
        roll_no = self.env['ir.sequence'].next_by_code(
                'roll.no.seq')
        self.write({'roll_no':roll_no})

    @api.onchange('is_student')
    def onchange_company_type1(self):
        super(ResPartner, self).onchange_company_type()
        if self.is_student == True:
            self.company_type = 'student'

    def _compute_company_type(self):
        for partner in self:
            if partner.is_student:
                partner.company_type = 'student'
            elif partner.is_company:
                partner.company_type = 'company'
            else:
                partner.company_type = 'person'

    @api.model
    def default_get(self, fields):
        res = super(ResPartner, self).default_get(fields)
        if self._context.get('is_student') == True:
            res.update({'is_student': True})
        return res


class StudentStandard(models.Model):
    _name = 'student.standard'
    _description = 'Student Standard'

    name = fields.Char('Standard')


class HowKnow(models.Model):
    _name = 'how.know'
    _description = 'How Know'

    name = fields.Char('Name')

# student division


class StandardDivision(models.Model):
    _name = 'standard.division'
    _description = 'Standard Division'
    
    name = fields.Char('Division')

# academic year


class Year(models.Model):
    _name = 'year.year'
    _description = 'Year'

    name = fields.Char('Year')
