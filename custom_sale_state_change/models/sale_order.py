from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection=[
        ('draft', 'Request'),
        ('sent', 'Request Sent'),
        ('sale', 'Completed'),
        ('done', 'Locked'),
        ('cancel', 'Rejected'),
    ], string='Status')
