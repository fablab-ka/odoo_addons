# -*- coding: utf-8 -*-

from openerp import models, fields, api


class res_partner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    id_cards = fields.One2many(string="ID Cards", comodel_name="lab.id_cards", inverse_name="assigned_client")
    lab_membership = fields.Selection([('m', 'Member'), ('l', 'Labsitter'), ('m', 'Manager'), ('g', 'Guest')], string="Membership status")