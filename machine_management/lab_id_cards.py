# -*- coding: utf-8 -*-

from openerp import models, fields, api


class machine_management2(models.Model):
    _name = 'lab.id_cards'

    card_id = fields.Char(string="Card Number", required=True)
    assigned_client = fields.Many2one(comodel_name="res.partner", string="Assigned client")
    status = fields.Selection([('u', 'unassigned'), ('a', 'active'), ('i', 'inactive')],
                              string='Status', default='a', required=True)
    card_type = fields.Selection([('1', 'Serial Number'), ('2', 'Type 2'), ('3', 'Type 3')], default='1', string="Card Type", required=True)

    @api.onchange('card_id')
    @api.depends('card_id')
    def _check_change(self):
        if self.card_id:
            self.card_id = self.card_id.replace(' ', '').upper()

    @api.one
    @api.constrains('assigned_client', 'status')
    def _check_can_be_active(self):
        if (self.assigned_client == False) and (self.status == 'active'):  # TODO: Doesn't work :(
            raise Warning('Cannot have active card without assigned user!')

    _sql_constraints = [
        ('card_id_unique', 'unique(card_id)', 'There already exists a Card with that ID!')
    ]