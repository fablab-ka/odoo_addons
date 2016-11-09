# -*- coding: utf-8 -*-

from openerp import models, fields, api


class machine_job(models.Model):
    _name = 'lab.access'

    machine = fields.Many2one(string="Machine", comodel_name="lab.machine", required=True)
    user = fields.Many2one(string="User", comodel_name="res.partner", required = True)
    start_time = fields.Datetime(string="Start time", required=True)
    end_time = fields.Datetime(string="End time")

