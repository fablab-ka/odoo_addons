import ldap
import logging
from ldap.filter import filter_format
from odoo import api, fields, models, tools

_logger = logging.getLogger(__name__)


class CompanyLDAP(models.Model):
    _name = 'res.company.ldap'
    _inherit = 'res.company.ldap'

    def map_ldap_attributes(self, conf, login, ldap_entry):
        """
        Compose values for a new resource of model res_users,
        based upon the retrieved ldap entry and the LDAP settings.
        :param dict conf: LDAP configuration
        :param login: the new user's login
        :param tuple ldap_entry: single LDAP result (dn, attrs)
        :return: parameters for a new resource of model res_users
        :rtype: dict
        """

        return {
            'name': ldap_entry[1]['cn'][0],
            'email': ldap_entry[1]['mail'][0],
            'login': login,
            'company_id': conf['company'][0]
        }


    @api.model
    def get_or_create_user(self, conf, login, ldap_entry):
        """
        Retrieve an active resource of model res_users with the specified
        login. Create the user if it is not initially found.

        :param dict conf: LDAP configuration
        :param login: the user's login
        :param tuple ldap_entry: single LDAP result (dn, attrs)
        :return: res_users id
        :rtype: int
        """

        user_id = False
        login = tools.ustr(login.lower().strip())
        self.env.cr.execute("SELECT id, active FROM res_users WHERE lower(login)=%s", (login,))
        res = self.env.cr.fetchone()
        if res:
            if res[1]:
                user_id = res[0]
                #ToDo: update access rights
        elif conf['create_user']:
            _logger.debug("Creating new Odoo user \"%s\" from LDAP" % login)
            values = self.map_ldap_attributes(conf, login, ldap_entry)
            SudoUser = self.env['res.users'].sudo()
            if conf['user']:
                values['active'] = True
                user_id = SudoUser.browse(conf['user'][0]).copy(default=values).id
            else:
                user_id = SudoUser.create(values).id
        return user_id
