from io import BytesIO
import base64
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import xlsxwriter


class ReportSaleOrder(models.Model):
    _name = 'report.sale.order'
    _description = 'Báo cáo theo dõi đơn hàng'

    date_start = fields.Date(default=lambda self: self._get_server_date())
    date_finish = fields.Date(default=lambda self: self._get_server_date())

    @api.constrains('date_start', 'date_finish')
    def check_date(self):
        for record in self:
            if record.date_start and record.date_finish:
                if record.date_finish < record.date_start:
                    raise ValidationError('Ngày kết thúc theo dõi bán hàng phải lớn hơn ngày bắt đầu!')

    def _get_server_date(self):
        # Lấy ngày hiện tại theo múi giờ của máy chủ
        server_date = fields.Date.today()
        return server_date

    def get_report_values(self):
        output = BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet("Sales Order Tracking")

        title_format = workbook.add_format({'bold': True, 'font_size': 20, 'font_name': 'Time New Roman'})
        title_format.set_align('center')
        worksheet.merge_range('A1:M1', 'Theo dõi đơn hàng', title_format)
        date_format = workbook.add_format({'bold': True, 'font_size': 16, 'font_name': 'Time New Roman'})
        header_format = workbook.add_format({'bold': True, 'bg_color': '#F2F2F2'})
        worksheet.write_string('A3:M3', f'Từ:{self.date_start} Đến: {self.date_finish}', date_format)
        title_format.set_align('center')
        worksheet.write_row('A5', ['Mã đơn hàng', 'Tổng đơn hàng', 'Đơn giá phải trả'], header_format)

        self._cr.execute("""
                    SELECT name, amount_untaxed + amount_tax as total_amount, amount_total
                    FROM sale_order
                    WHERE date_order BETWEEN %s AND %s
                """, (self.date_start, self.date_finish))
        orders = self._cr.fetchall()

        row = 7
        for order in orders:
            worksheet.write(row, 0, order[0])  # Mã đơn hàng
            worksheet.write(row, 1, order[1])  # Tổng đơn hàng
            worksheet.write(row, 2, order[2])  # Tổng phải trả
            row += 1

        workbook.close()

        # store_db
        attachment_id = self.env['ir.attachment'].create({
            'name': 'Theo dõi đơn hàng.xlsx',
            'datas': base64.b64encode(output.getvalue()),
            'type': 'binary',
            'res_model': self._name,
            'res_id': self.id,
        })

        # download
        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/' + str(attachment_id.id) + '?download=true',
            'target': 'new'
        }
