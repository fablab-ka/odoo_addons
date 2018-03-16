import odoo.addons.auth_signup.controllers.main as main
from odoo import api, fields, models, tools
import ldap
from ldap import modlist
import logging
from ldap.filter import filter_format
_logger = logging.getLogger(__name__)


class AuthSignupHome(main.Home):

    def _signup_with_values(self, token, values):
        print("test!" + str(token) + str(values))
        Ldap = main.request.env['res.company.ldap']
        for conf in Ldap.get_ldap_dicts():
            if Ldap.create_entry(conf, values['name'], values['login'], values['password']):
                print("LDAP entry created!")
                main.request.env.cr.commit()  # as authenticate will use its own cursor we need to commit the current transaction
                #uid = main.request.session.authenticate(values.db, values.login, values.password)
                return
        raise
        db, login, password = main.request.env['res.users'].sudo().signup(values, token)

        main.request.env.cr.commit()     # as authenticate will use its own cursor we need to commit the current transaction
        uid = main.request.session.authenticate(db, login, password)
        if not uid:
            raise SignupError(_('Authentication Failed.'))

class CompanyLDAP(models.Model):
    _inherit = 'res.company.ldap'

    def create_entry(self, conf, name, email, password):
        """
        :param dict conf: LDAP configuration
        :param name: Name of the Entry to create
        :param email: Email of the Entry to create
        :param attributes: email, password, ... of entry
        :return: true if success
        """

        try:
            conn = self.connect(conf)
            ldap_password = conf['ldap_password'] or ''
            ldap_binddn = conf['ldap_binddn'] or ''

            conn.simple_bind_s(ldap_binddn.encode('utf-8'), ldap_password.encode('utf-8'))

            dn = "cn=" + email + "," + conf['ldap_base']
            mod_list = {
                "objectClass": ["inetOrgPerson"],
                "cn": [str(name).encode('utf-8')],
                "sn": [str(name.split(' ')[-1]).encode('utf-8')],
                "mail": [str(email).encode('utf-8')],  # IA5
            }

            conn.add_s(dn, modlist.addModlist(mod_list))
            conn.passwd_s(dn, None, str(password))
            conn.unbind()

        except ldap.INVALID_CREDENTIALS:
            _logger.error('LDAP bind failed.')
            return
        except ldap.LDAPError, e:
            _logger.error('An LDAP exception occurred: %s', e)
            return
        return True

    def connect(self, conf):
        uri = 'ldap://%s:%d' % (conf['ldap_server'], conf['ldap_server_port'])

        connection = ldap.initialize(uri, bytes_mode=False)
        #connection.protocol_version = ldap.VERSION3
        if conf['ldap_tls']:
            connection.start_tls_s()
        return connection


class BaseConfigSettings(models.TransientModel):
    _inherit = 'base.config.settings'

    create_ldap_users = fields.Boolean(string="LDAP Create", help="Allow the creation of LDAP-Entries when registering new users")