# -*- coding: utf-8 -*-

from openerp import models, fields, api


class lab_machine(models.Model):
    _name = 'lab.machine'

    name = fields.Char(string="Name", required=True)
    status = fields.Selection([('r', 'running'), ('o', 'out of order'), ('n', 'not ready'), ('t', 'test phase')], string="Machine Status", required=True, default='n')
    rules = fields.Selection([('f', 'free for all'), ('r', 'restricted'), ('n', 'no access')], string="Access Rules", required=True, default='n')
    user_ids = fields.Many2many(string="Users", comodel_name="res.partner", relation="machine_user_relation", column1="machine_id", column2="user_id")
    owner_ids = fields.Many2many(string="Owners", comodel_name="res.partner", relation="machine_owner_relation", column1="machine_id", column2="owner_id")
    machine_tag_1 = fields.Many2one(comodel_name='product.tag', string="Product Tag 1",
                                    help="used for assigning products to the machine (eg for selling)")
    machine_tag_2 = fields.Many2one(comodel_name='product.tag', string="Product Tag 1",
                                    help="used for assigning products to the machine (eg for selling)")
