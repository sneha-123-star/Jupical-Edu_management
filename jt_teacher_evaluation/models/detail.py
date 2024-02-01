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
from odoo import api, fields, models, exceptions

class Templates (models.Model):
    _name = 'eval.detail'
    _rec_name ="description"
    _description = "Evaluation Details"

    description = fields.Char('Question')
    user_type = fields.Selection([('student', 'Student'),('teacher', 'Teacher'),('parent', 'Parent')], default='teacher')

class RatingRemarks(models.Model):
    _name = 'rating.remarks'
    _rec_name ="rating"

    rating = fields.Selection([('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),
        ('7','7'),('8','8'),('9','9'),('10','10')],default='0',string="Rating")
    remarks = fields.Selection([('poor','Poor'),('average','Average'),('good','Good'),('very_good','Very Good'),('excellent','Excellent')],string="Comments",default="good")


    @api.model
    def create(self, values):
        raise exceptions.ValidationError("Creation of new records for RatingRemarks is not allowed.")