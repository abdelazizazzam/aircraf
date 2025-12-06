from odoo import models, fields, api

class DiscountAmountMixin(models.AbstractModel):
    _name = 'discount.amount.mixin'

    discount_amount = fields.Float(string="Discount Amount", default=0.0)

    @api.onchange('discount_amount')
    def _onchange_discount_amount(self):
        for line in self:
            if line.price_unit:
                line.discount = (line.discount_amount / line.price_unit) * 100


class SaleOrderLine(models.Model):
    _inherit = ['sale.order.line', 'discount.amount.mixin']


class AccountMoveLine(models.Model):
    _inherit = ['account.move.line', 'discount.amount.mixin']
