# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.osv import osv, orm
import openerp.addons.decimal_precision as dp
from openerp.tools.translate import _
from openerp import tools
# class default_location(models.Model):
#     _name = 'default_location.default_location'

#     name = fields.Char()

class product_template(models.Model):
    _name = "product.template"
    _inherit = "product.template"

    default_location = fields.Many2one(string="Default Location", comodel_name="stock.location",
                                       help="Default stock location for this product")
    position = fields.Char(string="Location", size=12, help="Position of the product in the stock location.")

class stock_location(models.Model):
    _name = "stock.location"
    _inherit = "stock.location"

    default_products = fields.One2many(string="Products", comodel_name="product.template", inverse_name="default_location",
                                       help="List of products that are by default stored here.")

#Inspired by:
#https://github.com/ndp-systemes/odoo-addons/blob/8.0/product_putaway_last/product_putaway_last.py
class default_location_putaway_strategy(models.Model):
    _inherit = 'product.putaway'

    @api.cr_uid_context
    def _get_putaway_options(self, cr, uid, context=None):
        res = super(default_location_putaway_strategy, self)._get_putaway_options(cr, uid, context)
        res.append(('default', "Default Product Location"))
        return res

    method = fields.Selection(_get_putaway_options, "Method", required=True)

    @api.model
    def putaway_apply(self, putaway_strat, product):
        location = product.default_location;
        if putaway_strat.method == 'default' and location is not None:
            return location.id;
        else:
            return super(default_location_putaway_strategy, self).putaway_apply(putaway_strat, product)

class default_stock_change(osv.osv_memory):
    _inherit = "stock.change.product.qty"


    def default_get(self, cr, uid, fields, context):
        """ To get default values for the object.
         @param self: The object pointer.
         @param cr: A database cursor
         @param uid: ID of the user currently logged in
         @param fields: List of fields for which we want default values
         @param context: A standard dictionary
         @return: A dictionary which of fields with values.
        """
        res = super(default_stock_change, self).default_get(cr, uid, fields, context=context)
        product = self.pool.get('product.product').browse(cr, uid, res['product_id'])
        location = product.default_location.id

        if location:
            res['location_id'] = location
        return res