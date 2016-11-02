# -*- coding: utf-8 -*-

from openerp import models, fields, api


class res_partner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    id_cards = fields.One2many(string="ID Cards", comodel_name="lab.id_cards", inverse_name="assigned_client")
    lab_membership = fields.Selection([('m', 'Member'), ('l', 'Labsitter'), ('m', 'Manager'), ('g', 'Guest')], string="Membership status")


class product_product(models.Model):
    _name = "product.template"
    _inherit = "product.template"
    #_name = "product.product"
    #_inherit = "product.product"

    tag_ids = fields.Many2many(string="Tags", comodel_name="product.tag", relation="product_tag_relation2",
                               column1="product_id", column2="tag_id")
    #tag_ids = fields.Many2one(string="Tags", comodel_name="product.tag")


class product_tag(models.Model):
    _name = "product.tag"

    name = fields.Char(string="Name", required=True)
