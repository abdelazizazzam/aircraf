from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    discount_amount = fields.Float(string='Discount Amount', digits='Product Price')

    @api.onchange('discount_amount', 'price_unit', 'quantity')
    def _onchange_discount_amount(self):
        for line in self:
            try:
                qty = line.quantity or 1.0
                price = line.price_unit or 0.0
                subtotal = price * qty
                if subtotal and line.discount_amount:
                    line.discount = (line.discount_amount / subtotal) * 100.0
                else:
                    line.discount = 0.0
            except Exception:
                line.discount = 0.0
