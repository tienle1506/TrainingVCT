from odoo import http
import json


class WeatherController(http.Controller):
    @http.route('/weather', type='http', auth='public', website=True, methods=['GET'], csrf=False)
    def index(self, **kwargs):
        # print('Done')
        # day = int(kwargs.get('day', 1))
        # weather_records = http.request.env['weather'].search([], limit=day)
        #
        # weather_data = []
        # for record in weather_records:
        #     weather_data.append({
        #         'day_item': record.day_item,
        #         'date_item': record.date_item,
        #         'temp_hi': record.temp_hi,
        #         'temp_lo': record.temp_lo,
        #         'no_wrap1': record.no_wrap1,
        #         'no_wrap2': record.no_wrap2,
        #         'precip_content': record.precip_content,
        #     })
        # # response = json.dumps(weather_data)
        # # print(response)
        # # return response
        # print(weather_data)
        return http.request.render('vct_weather.weathers', {
        })

    @http.route('/api/weather/', type='http', auth='public', website=True, methods=['GET'], csrf=False)
    def return_response(self, **kwargs):
        day = int(kwargs.get('day', 1))
        weather_records = http.request.env['weather'].search([], limit=day)

        weather_data = []
        for record in weather_records:
            weather_data.append({
                'day_item': record.day_item,
                'date_item': record.date_item,
                'temp_hi': record.temp_hi,
                'temp_lo': record.temp_lo,
                'no_wrap1': record.no_wrap1,
                'no_wrap2': record.no_wrap2,
                'precip_content': record.precip_content,
            })
        response = json.dumps(weather_data)
        # print(response)
        return response
