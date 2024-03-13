from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class ResPartner(models.Model):
    _inherit = 'res.partner'

    config_code = fields.Char(string='Mã khuyến mãi')

    @api.onchange('config_code')
    def check_config_code(self):
        if self.config_code:
            if not re.match(r'^VIP_(100|[1-9][0-9]?)$', self.config_code):
                raise ValidationError('Not Valid Code')