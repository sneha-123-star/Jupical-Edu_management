from odoo import fields,models,api,_
from odoo.exceptions import ValidationError


class AdmissionInquiry(models.Model):

    _name = 'admission.inquiry'
    _description = 'Student Admission Inquiry Details'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    

    name = fields.Char(string="Name")
    fname = fields.Char(string="Father Name")
    mname = fields.Char(string="Mother Name")
    surname = fields.Char(string="surname")
    mobile = fields.Char(string="mobile")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    city = fields.Char(string="city")
    gr_no = fields.Char(string="Gr No.",tracking=True)
    zip_code = fields.Char(string="zip")
    add1 = fields.Text(string="Address 1")
    add2 = fields.Text(string="Address 2")
    standard_id = fields.Many2one('student.standard', 'Standard')
    howknow_id = fields.Many2one('how.know', 'How Student Know Our School')
    state_id = fields.Many2one('res.country.state', 'State')
    country_id = fields.Many2one('res.country', 'Country')
    div_id = fields.Many2one('standard.division', 'Division')
    year_id = fields.Many2one('year.year', 'Year')
    note = fields.Text("Note")
    birthdate = fields.Date("Birthdate")
    sel_gen = fields.Selection(
        [("male", "Male"), ("female", "Female")], default="male", string="Gender"
    )
    state = fields.Selection(
        [("draft", "Draft"), ("confirm", "Confirmed"), ("cancel", "Cancelled")], default="draft", string="State",tracking=True
    )

    def confirm_reservation_inq(self):
        for inq in self:
            if not inq.gr_no:
                raise ValidationError(_('Enter GR No. First'))
            vals={
            'is_student':True,
            'gender':inq.sel_gen,
            'name':inq.name,
            'father_name':inq.fname,
            'mother_name':inq.mname,
            'surname':inq.surname,
            'phone':inq.phone,
            'mobile':inq.mobile,
            'email':inq.email,
            'street':inq.add1,
            'street2':inq.add2,
            'city':inq.city,
            'state_id':inq.state_id.id,
            'howknow_id':inq.howknow_id.id,
            'zip':inq.zip_code,
            'country_id':inq.country_id.id,
            'gr_no':inq.gr_no,
            'curr_year':inq.year_id.id,
            'standard':inq.standard_id.id,
            'standard':inq.standard_id.id,
            'div':inq.div_id.id,
            'birthdate':inq.birthdate,
            'comment':inq.note,
            }
            stud_id = self.env['res.partner'].create(vals)

        self.state = 'confirm'

    def cancel_reservation_inq(self):
        self.state = 'cancel'
