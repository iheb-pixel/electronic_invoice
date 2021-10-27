# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.http import request
from datetime import datetime, timedelta


class AccountMove(models.Model):
    _inherit = 'account.invoice'

    qr_image = fields.Binary("QR Code", compute='_generate_qr_code')

    # @api.depends('state','company_id.name', 'company_id.vat','amount_total','invoice_date','amount_tax')
    def _generate_qr_code(self):
        for rec in self:
            if rec.number and rec.id and rec.state != 'draft':
                invoice_date = datetime.strftime(self.date_invoice, '%Y-%m-%d')
                data = {'Supplier': self.company_id.name, 'Supplier Tax ID': self.company_id.vat,
                        'Total with Taxes': str(self.amount_total) + ' ' + str(self.company_id.currency_id.name),
                        'Date Invoice': invoice_date,
                        'Total Taxes': str(self.amount_tax) + ' ' + str(self.company_id.currency_id.name)}
                rec.qr_image = request.env['qr.generator'].get_qr_code(data)
            else:
                rec.qr_image = None

    def change_number(self):
        ch = ''
        for rec in self.partner_id.vat:
            if rec == "١":
                ch = ch + '1'
            if rec == "٠":
                ch = ch + '0'
            if rec == "٢":
                ch = ch + '2'
            if rec == "٣":
                ch = ch + '3'
            if rec == "٤":
                ch = ch + '4'
            if rec == "٥":
                ch = ch + '5'
            if rec == "٦":
                ch = ch + '6'
            if rec == "٧":
                ch = ch + '7'
            if rec == "٨":
                ch = ch + '8'
            if rec == "٩":
                ch = ch + '9'
            if len(ch) == 0:
                return self.partner_id.vat
            else:
                return ch
