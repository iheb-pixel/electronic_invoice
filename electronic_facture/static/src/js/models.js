odoo.define('electronic_facture.models', function (require) {
"use strict";
var rpc = require('web.rpc');

var models = require('point_of_sale.models');
var _super_order = models.Order.prototype;

models.Order = models.Order.extend({

    export_for_printing: function() {
        var receipt = _super_order.export_for_printing.apply(this,arguments);
        
        // SCANER DATAS
        var company = receipt.company.name
        var company_vat = receipt.company.vat
        var total_with_tax = receipt.total_with_tax
        var date_inv = receipt.date.localestring
        var total_tax = receipt.total_tax
        
		rpc.query({
		    model: 'qr.generator',
		    method: 'get_qr_code',
		    args: [{'Supplier': company, 'Supplier Tax ID': company_vat , 'Total with Taxes': total_with_tax, 'Date Invoice': date_inv, 'Total Taxes': total_tax}]})
		    .then(function(result) {
					document.getElementById("ItemPreview").src = "data:image/png;base64," + result;
		    });


        return receipt;
    },

});

});

