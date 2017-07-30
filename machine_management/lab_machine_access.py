# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import datetime

class machine_job(models.Model):
    _name = 'lab.access'

    machine = fields.Many2one(string="Machine", comodel_name="lab.machine", required=True)
    client = fields.Many2one(string="Client", comodel_name="res.partner", required = False)
    user = fields.Many2one(string="User", comodel_name="res.partner", required = True)
    start_time = fields.Datetime(string="Start time", required=True)
    end_time = fields.Datetime(string="End time", required=True)
    sale_order_id = fields.Many2one(string="Sale Order", comodel_name="sale.order")
    duration = fields.Float(string="Duration (min.)", store=True, default=0)
    info = fields.Text(string="Info")

