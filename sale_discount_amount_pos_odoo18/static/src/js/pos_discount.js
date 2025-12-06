odoo.define('sale_discount_amount_pos.pos_discount', function(require){
    'use strict';
    var models = require('point_of_sale.models');
    try {
        var Orderline = models.Orderline;
        Orderline = Orderline.extend({
            set_discount_amount: function(amount){
                this.discount_amount = parseFloat(amount) || 0;
                var price_unit = (this.get_unit_price && this.get_unit_price()) || (this.get_price && this.get_price()) || this.price;
                var qty = (this.get_quantity && this.get_quantity()) || this.quantity || 1;
                var subtotal = (price_unit || this.price) * (qty || 1);
                if (subtotal > 0){
                    var percent = (parseFloat(this.discount_amount) / subtotal) * 100.0;
                    this.set_discount(percent);
                } else {
                    this.set_discount(0);
                }
            },
        });
    } catch (e){
        console.error('sale_discount_amount_pos: cannot extend Orderline', e);
    }
});
