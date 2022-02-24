# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        Módulo de gestión de cursos.""",

    'description': """
        Módulo de gestión de cursos
    """,

    'author': "Sergio Fraga",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/openacademy.xml',
        'views/templates.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    #'demo': [
     #   'demo/demo.xml',
    #],
}
