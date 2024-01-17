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
from odoo import fields,models,api,_
from odoo.exceptions import ValidationError


class CourseCourse(models.Model):

    _name = 'course.course'
    _description = 'Student Course Details'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    fee = fields.Float(string="Fee")
    rating = fields.Selection([('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5')],default='0',string="Rating")
    state = fields.Selection([('publish','Publish'),('draft','Draft')],default='draft',string="state")
    img = fields.Binary(string="Cover Image")