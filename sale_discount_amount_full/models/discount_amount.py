from odoo import models, fields, api

class DiscountAmountMixin(models.AbstractModel):
    _name = 'discount.amount.mixin'
    _description = 'Mixin for discount amount support'

    discount_amount = fields.Float(string='Discount Amount', digits='Product Price', default=0.0)

    @api.onchange('discount_amount', 'price_unit')
    def _onchange_discount_amount(self):
        for line in self:
            try:
                price = line.price_unit or 0.0
                if price:
                    # convert amount to percent relative to unit price
                    line.discount = (line.discount_amount / price) * 100.0
                else:
                    line.discount = 0.0
            except Exception:
                line.discount = 0.0

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_amount = fields.Float(string='Discount Amount', digits='Product Price')

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    discount_amount = fields.Float(string='Discount Amount', digits='Product Price')
