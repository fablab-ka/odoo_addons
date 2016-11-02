# -*- coding: utf-8 -*-
{
    'name': "Default Locations for Products",

    'summary': """
        Allows to give a product a default location in wich it will be placed automatically""",

    'description': """
        Gives products a default location. Locations show which products have set them as default location.
        When Updating Quantity on Hand, the default location gets selected as the Location to update.
        When using the put-away-strategy "Default Product Location", Products are put in their Default Location.

        This can be useful for very small enterprises and non-commercial audiences who want an easy stock management.

    """,

    'author': "Philip Caroli",
    'website': "https://fablab-karlsruhe.de",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}