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