odoo.define('sale_discount_amount_full.pos_discount', function(require){
    'use strict';
    const models = require('point_of_sale.models');

    // Safely extend Orderline prototype if exists
    try {
        const Orderline = models.Orderline;
        const _super = Orderline.prototype;
        models.Orderline = Orderline.extend({
            /**
             * Set discount by amount (currency units). This converts to percent internally.
             * @param {Number} amount - discount amount per unit
             */
            set_discount_amount: function(amount){
                if (!amount) {
                    this.set_discount(0);
                    return;
                }
                const price = (this.get_unit_price && this.get_unit_price()) || (this.get_price && this.get_price()) || this.get_unit_price && this.get_unit_price();
                if (!price || price == 0) {
                    this.set_discount(0);
                    return;
                }
                const percent = (parseFloat(amount) / parseFloat(price)) * 100.0;
                this.set_discount(percent);
            },
        });
    } catch (e) {
        console.error('sale_discount_amount_full: failed to extend Orderline', e);
    }
});
