from odoo import api, models, _
from odoo.exceptions import ValidationError


class Users(models.Model):
    _inherit = "res.users"

    @api.constrains('groups_id')
    def _check_one_user_type(self):
        super(Users, self)._check_one_user_type()

        h1 = self.env.ref('jt_education_base.group_school', False)
        h2 = self.env.ref('jt_education_base.group_college', False)

        if not h1 or not h2:
            # A user cannot be in a non-existant group
            return

        for user in self:
            if user._has_multiple_groups([h1.id, h2.id]):
                raise ValidationError(_("A user cannot have both School and College.\n"))
