# -*- coding: utf-8 -*-
# from odoo import http


# class VctWeather(http.Controller):
#     @http.route('/vct_weather/vct_weather/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vct_weather/vct_weather/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vct_weather.listing', {
#             'root': '/vct_weather/vct_weather',
#             'objects': http.request.env['vct_weather.vct_weather'].search([]),
#         })

#     @http.route('/vct_weather/vct_weather/objects/<model("vct_weather.vct_weather"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vct_weather.object', {
#             'object': obj
#         })
