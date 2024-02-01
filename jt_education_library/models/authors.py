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


class Authors(models.Model):
    _name = "authors.authors"
    _description = "Authors Details"

    # image_1920 = fields.Binary(
    #     related='partner_id.image_1920', store=True, attachement=True)
    authors_code = fields.Char(string="Author ID" ,copy=False)
    partner_id = fields.Many2one('res.partner', string="Author Name")
    name = fields.Char(related='partner_id.name', string="Name", store=True)
    street = fields.Char(related="partner_id.street", readonly=False)
    street2 = fields.Char(related="partner_id.street2", readonly=False)
    city = fields.Char(related="partner_id.city", readonly=False)
    state_id = fields.Many2one(related="partner_id.state_id", readonly=False)
    country_id = fields.Many2one(related="partner_id.country_id", readonly=False)
    phone = fields.Char(related="partner_id.phone", readonly=False)
    mobile = fields.Char(related="partner_id.mobile", readonly=False)
    email = fields.Char(related="partner_id.email", readonly=False)
    website = fields.Char(related="partner_id.website", readonly=False)
    is_author = fields.Boolean("Is a Author")
    publisher = fields.Char('Publisher')

    @api.model
    def create(self, vals):
        res = super(Authors, self).create(vals)
        res.authors_code = self.env['ir.sequence'].next_by_code('authors.seq')
        return res
