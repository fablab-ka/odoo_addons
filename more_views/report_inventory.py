# -*- coding: utf-8 -*-

import babel.dates
import re
import werkzeug
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from odoo import models, fields, http, _
from odoo.addons.website.models.website import slug
from odoo.http import request


class WebsiteEventController(http.Controller):
    @http.route(['/prod/<sn>'], type='http', auth="public", website=True)
    def products(self, sn, **searches):
        Lot = request.env['stock.production.lot']
        return "Nothing to see here now! <br> Serial Number: " + sn

class stock_production_lot(models.Model):
    _inherit = "product.tag"

    name = fields.Char(string="Name", required=True)
    products = fields.Many2many(comodel_name="product.template", string="Products")