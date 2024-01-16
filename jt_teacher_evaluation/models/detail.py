from odoo import fields, models

class Templates (models.Model):
    _name = 'eval.detail'
    _rec_name ="description"

    description = fields.Char('Question')
    user_type = fields.Selection([('student', 'Student'),('teacher', 'Teacher'),('parent', 'Parent')], default='teacher')

class RatingRemarks(models.Model):
    _name = 'rating.remarks'
    _rec_name ="rate"

    rate = fields.Float("Ratings")
    remarks = fields.Selection([('poor','Poor'),('average','Average'),('good','Good'),('very_good','Very Good'),('excellent','Excellent')],string="Comments",default="good")