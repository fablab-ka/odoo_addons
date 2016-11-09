# -*- coding: utf-8 -*-
{
    'name': "Machine Management",

    'summary': """
        Manages the state of machines and their access rights.""",

    'description': """
Machine Management
==============
Allows Machine Management
TODO: Write more stuff
    """,

    'author': "Philip Caroli",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Lab Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'lab_machine.xml',
        'lab_id_cards.xml',
        'small_mods.xml',
        'lab_machine_access.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}