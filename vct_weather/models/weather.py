from odoo import models, fields


class Weather(models.Model):
    _name = 'weather'
    _description = 'Dự báo thời tiết'

    day_item = fields.Text()
    date_item = fields.Text()
    temp_hi = fields.Text()
    temp_lo = fields.Text()
    no_wrap1 = fields.Text()
    no_wrap2 = fields.Text()
    precip_content = fields.Text()
