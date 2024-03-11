from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class MassActionUpdateCodeforCus(models.Model):
    _name = 'mass.action.update.code'
    _description = 'Mass Action Update Code'

    new_code_update = fields.Char(string='Mã khuyến mãi', requied=True )

    @api.constrains('new_code_update')
    def check_config_code(self):
        if self.new_code_update:
            if not re.match(r'^VIP_(100|[1-9][0-9]?)$', self.new_code_update):
                raise ValidationError('Not Valid Code')

    def update_code_for_cus(self):
        selected_records = self.env.context.get('active_ids', [])
        records_to_update = self.env['res.partner'].browse(selected_records)

        for record in records_to_update:
            record.write({
                'config_code': self.new_code_update})
