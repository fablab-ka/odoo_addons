# -*- coding: utf-8 -*-
{
    'name': "More Views",

    'summary': """
        Adds more views and forms:
        - simple Event form
        
        """,

    'description': """
More Views
========================================
Adds more views and forms:
- simple Event form
        
    """,

    'author': "Philip Caroli",
    'website': "http://www.fablab-karlsruhe.de",
    'category': 'Lab Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website_event', 'machine_management'],

    # always loaded
    'data': [
        "event.xml",
        "report_inventory.xml",
        #"report_invoice.xml"
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}