# -*- coding: utf-8 -*-
from openerp import http

# class DefaultLocation(http.Controller):
#     @http.route('/default_location/default_location/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/default_location/default_location/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('default_location.listing', {
#             'root': '/default_location/default_location',
#             'objects': http.request.env['default_location.default_location'].search([]),
#         })

#     @http.route('/default_location/default_location/objects/<model("default_location.default_location"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('default_location.object', {
#             'object': obj
#         })