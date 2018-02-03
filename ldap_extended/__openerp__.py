# -*- coding: utf-8 -*-
{
    'name': "Extended LDAP Interface",

    'summary': "additional functionallity for LDAP",

    'description': """
Extended LDAP Interface
========================================
DONE:
Uses displayName instead of SN for res.users name

PLANED:
Updates user groups that are based on LDAP groups on login.
This allows to change user access rights via LDAP after user creation on first login.

Also fixes a bug resulting in Partners based on LDAP to have their Email set to the template's Email.
    """,

    'author': "Philip Caroli",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['auth_ldap',],

    # always loaded
    'data': [
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}