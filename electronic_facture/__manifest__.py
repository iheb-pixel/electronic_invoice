# -*- coding: utf-8 -*-
{
    'name': 'Electronic FACTURE',
    'version': '12.0',
    'price': 5.99,
    'currency': 'EUR',
    'license': 'AGPL-3',
    'description': """
    this module help u to make a qr code code for accounting invoice repport and pos repport
    """,
    'category': 'accounting & Pos',
    'website': '',
    'depends': ['web', 'point_of_sale', 'account'],
    'data': [
        # Views
        'views/pos_template.xml',
        'views/account_invoice_view.xml',

        # Report
        'report/account_invoice_report_template.xml',
    ],

    'images': [
        'static/descriptions/qr_code_payment_icon_181835.png',
    ],

    'qweb': [

        'static/src/xml/Screens/ReceiptScreen/OrderReceipt.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
