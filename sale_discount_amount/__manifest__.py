{
    'name': 'Discount Amount on Lines',
    'version': '1.0',
    'summary': 'Use fixed amount discount instead of percentage on sale, invoice, and POS',
    'depends': ['sale_management', 'account'],
    'data': [
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
        # 'views/pos_res_company_view.xml',
    ],

}
