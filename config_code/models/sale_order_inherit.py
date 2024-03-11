from io import BytesIO

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import xlsxwriter


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = "Sales Order"

    conf_code_ref = fields.Char(string='Mã khuyến mãi', readonly=True)

    @api.onchange('partner_id')
    def onchange_for_cus_code(self):
        for order in self:
            if order.partner_id.config_code:  # Kiểm tra nếu khách hàng có config_code
                order.conf_code_ref = order.partner_id.config_code

    @api.depends('order_line.price_total')
    def _my_amount_all(self):
        """
        Compute the total amounts order
        """
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            if self.conf_code_ref:
                code = int(self.conf_code_ref.split('_')[1])
                print(code)
                # Add your custom logic here to modify amount_total, amount_untaxed, amount_tax if needed
                order.update({
                    'amount_untaxed': amount_untaxed,
                    'amount_tax': amount_tax,
                    'amount_total': (amount_untaxed + amount_tax) - (amount_untaxed + amount_tax) * (code / 100),
                })
            else:
                order.update({
                    'amount_untaxed': amount_untaxed,
                    'amount_tax': amount_tax,
                    'amount_total': amount_untaxed + amount_tax,
                })

    amount_untaxed = fields.Monetary(string='Untaxed Amount', store=True, readonly=True, compute='_my_amount_all',
                                     tracking=5)
    amount_tax = fields.Monetary(string='Taxes', store=True, readonly=True, compute='_my_amount_all')
    amount_total = fields.Monetary(string='Total', store=True, readonly=True, compute='_my_amount_all', tracking=4)

