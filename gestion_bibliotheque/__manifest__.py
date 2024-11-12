# -*- coding: utf-8 -*-
{
    'name': "gestion_bibliotheque",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
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
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/auteur_view.xml',
        'views/emprunt_view.xml',
        'views/emprunteur_view.xml',
        'views/livre_view.xml',
        'wizards/add_emprunt_wizard_views.xml',
        'wizards/view_reset_emprunts_wizard_form.xml',
    ],
    'application': True,
}
