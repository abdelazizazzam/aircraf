{'name': 'Discount Amount on Lines (Odoo 18)',
 'version': '1.0', 'category': 'Sales',
 'summary': 'Allow entering discount as fixed amount on sale/invoice lines and POS helper',
 'author': 'Generated for Abdelaziz',
 'depends': ['sale_management', 'account', 'point_of_sale'],
 'data': ['security/ir.model.access.csv'],
 'assets':
     {'point_of_sale.assets':
                ['sale_discount_amount_full/static/src/js/pos_discount.js']
            },
 'installable': True,
 'application': False, 'auto_install': False}
