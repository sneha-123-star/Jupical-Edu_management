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
from odoo import models, fields, api


class Books(models.Model):

    _name = "books.books"
    _description = "Books Details"
    _rec_name = 'name'
    _sql_constraints = [('name_uniq', 'unique (name)',
                         'Book Name Must Be Unique !')]

    # @api.multi
    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s - %s' % (rec.name, rec.author.name)))
        return res

    @api.model
    def create(self, vals):
        res = super(Books, self).create(vals)
        res.books_code = self.env['ir.sequence'].next_by_code('books.seq')
        return res

    # Details of Books
    books_image = fields.Binary(
        "Book Cover Picture", attachement=True, store=True)
    name = fields.Char("Name", required=True)
    no_of_books = fields.Integer('Total No. Of Books')
    lang_id = fields.Many2many('book.language', string='Language')
    edition = fields.Float(string="Edition")
    book_ids = fields.Many2many("book.xls.report", string="Book Ids")
    genres = fields.Selection([
        ('romance', 'Romance'),
        ('horror', 'Horror'),
        ('mystery', 'Mystery'),
        ('historic', 'Historic'),
        ('biography', 'Biography'),
        ('science', 'Science'),
        ('cooking', 'Cooking'),
        ('art', 'Art'),
        ('motivational', 'Motivational'),
        ('child', 'Child'),
        ('comic', 'Comic')], default="motivational", string='Genres')
    author = fields.Many2one("authors.authors", string="Author")
    # , default=lambda self: self.env['ir.sequence'].next_by_code('books.seq')
    books_code = fields.Char(string="Book ID" ,copy=False)
    no_of_books_issued = fields.Integer('No. Of Books Issued', compute='_compute_no_of_books_issued')
    no_of_books_lost = fields.Integer('No. Of Books Lost', compute='_compute_no_of_books_lost')
    no_of_books_available = fields.Integer('No. Of Books Available', compute='_compute_no_of_books_available')

    def _compute_no_of_books_issued(self):
        for rec in self:
            issuebook_data = self.env['issue.books'].search([('issuebookslines_ids.name.id','=',rec.id),('state','=','issued')])
            rec.no_of_books_issued = len(issuebook_data)

    def _compute_no_of_books_lost(self):
        for rec in self:
            lostbook_data = self.env['issue.books'].search([('issuebookslines_ids.name.id','=',rec.id),('state','=','lost')])
            rec.no_of_books_lost = len(lostbook_data)

    def _compute_no_of_books_available(self):
        for rec in self:
            rec.no_of_books_available = rec.no_of_books - (rec.no_of_books_issued + rec.no_of_books_lost)

class BookLanguage(models.Model):
    _name = 'book.language'

    name = fields.Char(string="Name")
    