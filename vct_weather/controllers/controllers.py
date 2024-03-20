from odoo import http
import json
import datetime


class WeatherController(http.Controller):
    @http.route('/weather', type='http', auth='public', website=True, methods=['GET'], csrf=False)
    def index(self, **kwargs):
        return http.request.render('vct_weather.weathers', {
        })

    @http.route('/api/weather/', type='http', auth='public', website=True, methods=['GET'], csrf=False)
    def return_response(self, **kwargs):
        day = int(kwargs.get('day', 1))
        now_day = datetime.datetime.strptime(datetime.date.today().strftime('%m/%d'), '%m/%d')
        while True:
            day = day + 1
            weather_records = http.request.env['weather'].search([], limit=day)
            weather_data = []
            for record in weather_records:
                record_date = datetime.datetime.strptime(record.date_item, '%m/%d')
                if record_date >= now_day:
                    weather_data.append({
                        'day_item': record.day_item,
                        'date_item': record.date_item,
                        'temp_hi': record.temp_hi,
                        'temp_lo': record.temp_lo,
                        'no_wrap1': record.no_wrap1,
                        'no_wrap2': record.no_wrap2,
                        'precip_content': record.precip_content,
                    })
                if len(weather_data) == int(kwargs.get('day')):
                    break
            if len(weather_data) == int(kwargs.get('day')):
                break
        response = json.dumps(weather_data)
        print(response)
        return response
