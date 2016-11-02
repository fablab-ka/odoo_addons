# -*- coding: utf-8 -*-

from openerp import models, fields, api


class machine_job(models.Model):
    _name = 'lab.job'

    machine = fields.One2many(string="Machine", required=True)
    start_time = fields.Datetime(string="Start time")
    end_time = fields.DateTime(string="Stop time")
