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

class TimeTable(models.Model):

	_name = "student.timetable"
	_description = "Student Timetable"

	name = fields.Char(compute='get_name')
	standard = fields.Many2one('student.standard', string="Standard")
	division = fields.Many2one('standard.division', string='Division')
	curr_year = fields.Many2one('year.year', string='Academic Year')
	timetable_mon = fields.One2many('student.timetable.line', 'timetable_id',
									domain=[('week_day', '=', '0')])
	timetable_tue = fields.One2many('student.timetable.line', 'timetable_id',
									domain=[('week_day', '=', '1')])
	timetable_wed = fields.One2many('student.timetable.line', 'timetable_id',
									domain=[('week_day', '=', '2')])
	timetable_thur = fields.One2many('student.timetable.line', 'timetable_id',
									 domain=[('week_day', '=', '3')])
	timetable_fri = fields.One2many('student.timetable.line', 'timetable_id',
									domain=[('week_day', '=', '4')])
	timetable_sat = fields.One2many('student.timetable.line', 'timetable_id',
									domain=[('week_day', '=', '5')])
	timetable_sun = fields.One2many('student.timetable.line', 'timetable_id',
									domain=[('week_day', '=', '6')])
	student_ids = fields.Many2many('res.partner', string='Student',domain=[('is_student', '=', True)])

	def get_name(self):
		"""To generate name for the model"""
		for i in self:
			if i.standard and i.division and i.curr_year:
				i.name = str(i.standard.name) + "/" + \
						 str(i.division.name) + "/" + str(i.curr_year.name)
			else:
				i.name =''

class TimeTableLine(models.Model):

	_name = "student.timetable.line"
	_description = "Student Timetable Line"

	period_id = fields.Many2one('timetable.period', string="Period")
	time_from = fields.Float(related = "period_id.time_from")
	time_till = fields.Float(related = "period_id.time_to")
	subject = fields.Many2one('student.subject', string='Subjects')
	faculty_id = fields.Many2one('res.partner', string='Faculty',domain=[('is_faculty', '=', True)])
	week_day = fields.Selection([
		('0', 'Monday'),
		('1', 'Tuesday'),
		('2', 'Wednesday'),
		('3', 'Thursday'),
		('4', 'Friday'),
		('5', 'Saturday'),
		('6', 'Sunday'),
	], 'Day')
	timetable_id = fields.Many2one('student.timetable')
	date = fields.Date("Date")

class TimetablePeriod(models.Model):
	_name = 'timetable.period'
	_description = 'Timetable Period'

	name = fields.Char(string="Name")
	time_from = fields.Float(string='From')
	time_to = fields.Float(string='To')
