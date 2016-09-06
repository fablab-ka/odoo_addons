# -*- coding: utf-8 -*-
from openerp import http

# class MachineManagement(http.Controller):
#     @http.route('/machine_management/machine_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/machine_management/machine_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('machine_management.listing', {
#             'root': '/machine_management/machine_management',
#             'objects': http.request.env['machine_management.machine_management'].search([]),
#         })

#     @http.route('/machine_management/machine_management/objects/<model("machine_management.machine_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('machine_management.object', {
#             'object': obj
#         })