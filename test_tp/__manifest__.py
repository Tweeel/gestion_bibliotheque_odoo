# -*- coding: utf-8 -*-
{
    'name': "gestion_examen",

    'summary': "This module is only ment for the practice test 2024/2025",

    'description': """
This module is only ment for the practice test 2024/2025
    """,

    'author': "Houssam Eddine",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/etudiant_view.xml',
        'views/examen_view.xml',
        'views/salle_view.xml',
    ],
    'application': True,
}
