# -*- coding: utf-8 -*-
from openerp import http
import json
import datetime
import pytz


class MachineManagement(http.Controller):
    @http.route('/get_games/', auth='public')
    def get_games(self, **kw):
        product_templates = http.request.env['product.template'].search([])
        if product_templates:
            out = "["
            for t in product_templates:
                o = {
                    'name': t.name,
                    'image': t.image,
                }
                out += json.dumps(o) + ","
            out = out[:-1] + "]"
            return out
        else:
            return "[]"