# -*- coding: utf-8 -*-
from openerp import http
import json

class RalfPlugin(http.Controller):

    @http.route('/ralfsys/geld_einzahlen/<int:amount>/<int:user>', auth='public', type='http')
    def geld_einzahlen(self, amount, user, **kw):
        
        print('Geld Einzahlen: ' + str(amount) + '€ von ' + str(user))

#class MachineManagement(http.Controller):

    # @http.route('/machine_management/machine_management/test/', auth='public', type='http')
    # def index(self, **kw):
    #     product_templates = http.request.env['product.template'].search([])
    #     out = "return:"
    #     for t in product_templates:
    #         o = {
    #             'name': t.name,
    #             'price': t.list_price,
    #             'id': t.id
    #         }
    #         out += json.dumps(o)
    #     print out
    #     return ""
        #return json.dumps(product_templates[0])

#     @http.route('/machine_management/machine_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('machine_management.listing', {
#             'root': '/machine_management/machine_management',
#             'objects': http.request.env['machine_management.machine_management'].search([]),
#         })

    # @http.route('/machine_management/machine_management/objects/<model("machine_management.machine_management"):obj>/', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('machine_management.object', {
    #         'object': obj
    #     })