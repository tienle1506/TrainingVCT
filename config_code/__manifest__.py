# -*- coding: utf-8 -*-
{
    'name': 'Cấu hình mã khuyến mãi',
    'version': '1.0.0',
    'category': 'Sales/Sales',
    'author': 'Tien',
    'sequence': -100,
    'summary': 'Config Code',
    'description': """ ABC """,
    'depends': ['sale', 'base'],
    'assets': {
    },
    'data': [
        'reports/sale_report.xml',
        'wizard/mass_action_update_code_for_cus.xml',
        'views/customer_code.xml',
        'views/inherit_website_sale.xml',
        'views/menu.xml',
        'views/inherit_view_customer.xml',
        'views/inherit_view_sale_order.xml',
        'security/security.xml',

    ],
    'qweb': [
        'static/src/xml/template_button_export_report.xml', ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
