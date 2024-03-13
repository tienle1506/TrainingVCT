from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.http import request


class WebsietSaleCus(http.Controller):

    @http.route(['/shop/code'], type='http', auth="public", website=True, sitemap=False)
    def pricelist_cus(self, promo_code_input, **post):
        redirect = post.get('r', '/shop/cart')
        # empty promo code is used to reset/remove pricelist (see `sale_get_order()`)
        partner_id = (request.env.user).partner_id
        code = partner_id.config_code
        if promo_code_input:
            order = request.website.sale_get_order()
            print(order)
            if promo_code_input == code:
                request.env['sale.order'].sudo().apply_code(order, code)
                return request.redirect(post.get('r', '/shop/cart'))
            else:
                return request.redirect("%s?code_not_available=1" % redirect)
