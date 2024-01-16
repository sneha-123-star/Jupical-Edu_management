from odoo import fields, models, api, _

class ResCompany(models.Model):

	_inherit = 'res.company'

	authorised_signatory_id = fields.Many2one("res.partner", string="Authorised Person")
	namep = fields.Char(related="authorised_signatory_id.name")
	function = fields.Char(related="authorised_signatory_id.function")
	signature = fields.Binary("Signature")
	stamp_image = fields.Image('Stamp Image', copy=False, attachment=True, max_width=1024, max_height=1024)