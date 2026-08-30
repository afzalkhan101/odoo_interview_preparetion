
{
   'name': "book self",
   'version': '19.0.1.0.0',
   'summary': "Adds an approval workflow to the sales order process",
   'description': """
       This module adds an approval workflow to the sales order,
       and provides multi-level validation, notification and dashboard.
   """,
   'category': 'custom',
   'author': "BS",
   'website': "https://www.yourcompany.com",
   'license': 'LGPL-3',
   'depends': ['base', 'sale_management', 'mail'],
   'data': [
          'security/ir.model.access.csv',
          'views/book_list_views.xml',
          'views/menu_views.xml',
    #    'data/sale_order_approval_data.xml',
   ],

   'installable': True,
   'application': True,
   'auto_install': False,

}