# -*- coding: utf-8 -*-

from openerp import models, fields, api


class machine_management2(models.Model):
    _name = 'lab.id_cards'

    card_id = fields.Char(string="Card Number", required=True)
    assigned_client = fields.Many2one(comodel_name="res.partner", string="Assigned client")
    status = fields.Selection([('unassigned', 'unassigned'), ('active', 'active'), ('inactive', 'inactive')],
                              string='Status', default='unassigned', required=True)

    @api.one
    @api.constrains('assigned_client', 'status')
    def _check_can_be_active(self):
        if (self.assigned_client == False) and (self.status == 'active'):  # TODO: Doesn't work :(
            raise Warning('Cannot have active card without assigned user!')

class res_partner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    id_cards = fields.One2many(string="ID Cards", comodel_name="lab.id_cards", inverse_name="assigned_client")