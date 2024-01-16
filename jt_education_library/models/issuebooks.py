# -*- coding: utf-8 -*-
##############################################################################
#
#    AtharvERP Business Solutions
#    Copyright (C) 2020-TODAY AtharvERP Business Solutions(<http://www.atharverp.com>).
#    Author: AtharvERP Business Solutions(<http://www.atharverp.com>)
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
from odoo import models, fields, api, _
import datetime
from odoo.exceptions import ValidationError, Warning as UserError
import io
import base64
from xlwt import Workbook
from odoo.tools.misc import xlsxwriter

class IssuebooksLines(models.Model):

    _name = "issue.books.lines"
    _description = "Books Issued details."

    name = fields.Many2one("books.books", string="Book Name")
    issue_books = fields.Many2one("issue.books", string="Issue Books")
    author = fields.Many2one(related='name.author', string="Author")
    genres = fields.Selection(related='name.genres', string="Genres")
    lang_id = fields.Many2many(related='name.lang_id', string='Language')
    issuebookslines_image = fields.Binary(
        related='name.books_image', string="Book Cover Picture", attachement=True, store=True)

class Issuebooks(models.Model):

    _name = "issue.books"
    _description = "Books Issued details."

    @api.constrains('date_return')
    def date_constrains(self):
        date_issue = datetime.date.today()
        delta = (self.date_return - date_issue).days
        if delta > 7:
            raise ValidationError(
                'User Error, Maximum allowed days for issue books is 7 days!')

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s - %s' % ( rec.issuebooks_code,rec.student_id.name)))
        return res

    # Details of books issued.
    date_return = fields.Date("Date Of Return", required=True)
    datetime_issue = fields.Datetime(
        "Date & Time Of Issue", default=lambda self: fields.datetime.now())
    student_id = fields.Many2one(
        "res.partner", string="Students", domain=[('is_student', '=', True)], required=True)
    standard = fields.Many2one(
        related='student_id.standard', string="Standard")
    division = fields.Many2one(
        related='student_id.div', string="Division")
    roll_no = fields.Integer(
        related='student_id.roll_no', string="Roll No.", size=2)
    issuebooks_code = fields.Char(string="Issue ID" ,copy=False)
    issuebookslines_ids = fields.One2many(
        "issue.books.lines", "issue_books", string="Issue Book Lines")
    name = fields.Many2one(related='issuebookslines_ids.name')
    issuebooks_image = fields.Binary(
        related='issuebookslines_ids.issuebookslines_image')
    fine_detail = fields.Selection([
        ('lost', 'Due to Lost'),
        ('late', 'Due to Late Return')], string='Fine Reason')
    fine_amount = fields.Float(string="Fine Amount")
    fine_description = fields.Text('fine description')
    state = fields.Selection([
        ('issued', 'Issued'),
        ('returned', 'Returned'),
        ('lost', 'Lost'),
        ('cancel', 'Cancel')], default="issued", string="Issue Status", readonly=True)

    @api.onchange('issuebookslines_ids')
    def _onchange_issuebookslines_ids(self):
        for rec in self.issuebookslines_ids.name:
            if rec.no_of_books_available == 0:
                raise ValidationError(_('%s is not available!' % rec.name))

    def books_issued(self):
        self.ensure_one()
        self.state = 'issued'

    def books_returned(self):
        self.ensure_one()
        self.state = 'returned'

    def books_lost(self):
        self.ensure_one()
        self.state = 'lost'

    def books_cancel(self):
        self.ensure_one()
        self.state = 'cancel'

    @api.model
    def create(self, vals):
        res = super(Issuebooks, self).create(vals)
        res.issuebooks_code = self.env[
            'ir.sequence'].next_by_code('issuebooks.seq')
        return res

    def issuebook_xls_report_template(self):

        output = io.BytesIO()
        
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet(_('Issue Books Details'))
        header_style = workbook.add_format({'bold': True, 'align': 'center'})
        value = workbook.add_format({'align': 'left'})
        header_table = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': '#CCCCCC'})
        value_style1 = workbook.add_format({'bg_color': '#DDDDDD', 'align': 'center'})
        value_style2 = workbook.add_format({'bg_color': '#EEEEEE', 'align': 'center'})
        style = workbook.add_format()

        filename_1 = "Issue Books Details Report.xls"
        row = 0
        col = 0
        
        sheet.merge_range(row, col, row, 5, 'Issue Books Details',header_style)

        row = row + 2
        col = 0
        sheet.merge_range(row, col, 7, 5, '')
        if self.env.user and self.env.user.company_id and self.env.user.company_id.logo:
            filename = 'logo.png'
            image_data = io.BytesIO(base64.standard_b64decode(self.env.user.company_id.logo))
            sheet.insert_image(row,col, filename, {'image_data': image_data,'x_offset':8,'y_offset':3,'x_scale':0.1,'y_scale':0.1})

        address = ""
        partner = self.env.user.company_id.partner_id
        if partner:
            if partner.name:
                address += str(partner.name)
                address += '\n'
            if partner.street:
                address += '\n'
                address += str(partner.street)
            if partner.street2:
                address += '\n'
                address += str(partner.street2)
            if partner.city:
                address += '\n'
                address += str(partner.city)
                address += '-'
            if partner.zip:
                address += str(partner.zip)
            if partner.state_id:
                address += ','
                address += str(partner.state_id.name)
            if partner.phone:
                address += '\n'
                address += 'Phone No.:'
                address += str(partner.phone)
            if partner.email:
                address += '\n'
                address += 'Email:'
                address += partner.email
            if partner.vat:
                address += '\n'
                address += 'GSTIN NO.'
                address += partner.vat
        sheet.write(row,col,address,header_style)
        
        row += 7
        col = 0
        sheet.write(row,col,_('Student :'),header_table)
        sheet.write(row,col + 1,self.student_id.name,value)

        sheet.write(row,col + 2,_('Standard :'),header_table)
        sheet.write(row,col + 3,self.standard.name + "/" + self.division.name ,value)
        
        sheet.write(row,col + 4,_('Roll No. :'),header_table)
        sheet.write(row,col + 5,self.roll_no,value)

        row += 2
        col = 0
        sheet.write(row,col + 1,_('Issue Date :'),header_table)
        sheet.write(row,col + 2,str(self.datetime_issue),value)

        sheet.write(row,col + 3,_('Return Date :'),header_table)
        sheet.write(row,col + 4,str(self.date_return),value)


        row += 2
        col = 0
        sheet.set_column(col, col,10)
        sheet.write(row,col,_('Sr'),header_table)

        col +=1
        sheet.set_column(col, col,17)
        sheet.write(row,col,_('Book ID'),header_table)
        
        col +=1 
        sheet.set_column(col, col,25)
        sheet.write(row,col,_('Book Name'),header_table)
        
        col += 1
        sheet.set_column(col, col,17)
        sheet.write(row,col,_('Author'),header_table)
        
        col += 1
        sheet.set_column(col, col,10)
        sheet.write(row,col,_('Generes'),header_table)
        
        col += 1
        sheet.set_column(col, col,12)
        sheet.write(row,col,_('Book Status'),header_table)
        
        row += 1
        col = 0
        count = 1
        issue_lines = self.issuebookslines_ids

        for line in issue_lines:
            if row%2 == 0:
                style= value_style1
            else:
                style = value_style2

            sheet.write(row, col, count, style)

            sheet.write(
                row, col + 1, line.name.books_code  or '', style)

            sheet.write(
                row, col + 2, line.name.name or '', style)

            sheet.write(
                row, col + 3, line.author.name or '', style)

            sheet.write(
                row, col + 4, line.genres or '', style)

            sheet.write(
                row, col + 5, self.state or '', style)
            
            count = count + 1
            row += 1
        
        workbook.close()
        xlsx_data = base64.encodebytes(output.getvalue())
        res_id = self.env['issuebook.xls.report'].create(
            {'excel_file': xlsx_data, 'file_name': filename_1})

        return {
            'name': 'Issue Books Details',
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': False,
            'res_model': 'issuebook.xls.report',
            'domain': [],
            'type': 'ir.actions.act_window',
            'target': 'new',
            'res_id': res_id.id,
            'context': self._context,
        }

    def get_issue_mail_send(self):
        for issuebook_data in self.search([('state','=','issued')]):
            for employee in self.env['res.partner'].search([('id','=',issuebook_data.student_id.id), ('is_student','=', True)]):
                template_id = self.env.ref('jt_education_library.email_template_issuebooks_mail').id
                template_obj = self.env['mail.template'].browse(template_id)
                if template_obj:
                    template_obj.send_mail(issuebook_data.id, force_send=True)
    