# -*- coding: utf-8 -*-

from openerp import models, fields, api


class machine_management2(models.Model):
    _name = 'lab.id_cards'

    card_id = fields.Char(string="Card Number", required=True)
    assigned_client = fields.Many2one(comodel_name="res.partner", string="Assigned client")
    status = fields.Selection([('unassigned', 'unassigned'), ('active', 'active'), ('inactive', 'inactive')],
                              string='Status', default='unassigned', required=True)
    card_type = fields.Selection([('1', 'Type 1'), ('2', 'Type 2'), ('3', 'Type 3')], default='1', string="Card Type")

    @api.one
    @api.constrains('assigned_client', 'status')
    def _check_can_be_active(self):
        if (self.assigned_client == False) and (self.status == 'active'):  # TODO: Doesn't work :(
            raise Warning('Cannot have active card without assigned user!')
