# -*- coding: utf-8 -*-

from openerp import models, fields, api


class res_partner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    id_cards = fields.One2many(string="ID Cards", comodel_name="lab.id_cards", inverse_name="assigned_client")
    lab_membership = fields.Selection([('m', 'Member'), ('l', 'Labsitter'), ('m', 'Manager'), ('g', 'Guest')], string="Membership status")


class product_template(models.Model):
    _name = "product.template"
    _inherit = "product.template"
    #_name = "product.product"
    #_inherit = "product.product"
    #tag_ids = fields.Many2one(comodel_name='product.tag', string="Tag", delegate=True)
    #tag_ids = fields.Many2many(comodel_name='product.tag', string="Tags", relation='tag_product_rel', column1='id1', column2='id2')
    tag_ids = fields.Many2many(string="Tags", comodel_name="product.tag", delegate=True, help="Tag for assigning this Product to a machine.")
    machine_parameter_1 = fields.Char(string="Parameter 1", help="General purpose Parameter")
    machine_parameter_2 = fields.Char(string="Parameter 2", help="General purpose Parameter")
    machine_parameter_3 = fields.Char(string="Parameter 3", help="General purpose Parameter")
    machine_parameter_4 = fields.Char(string="Parameter 4", help="General purpose Parameter")

class product_tag(models.Model):
    _name = "product.tag"

    name = fields.Char(string="Name", required=True)
    products = fields.Many2many(comodel_name="product.template", string="Products")