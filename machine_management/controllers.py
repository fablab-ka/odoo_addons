# -*- coding: utf-8 -*-
from openerp import http
import json


class MachineManagement(http.Controller):
    @http.route('/machine_management/getProductByTag/<int:tag_id>/', auth='public')  # , type='http'
    def getProductByTag(self, tag_id, **kw):
        product_templates = http.request.env['product.template'].search([('tag_ids', '=', tag_id)])
        if product_templates:
            out = "["
            for t in product_templates:
                o = {
                    'name': t.name,
                    'price': t.list_price,
                    'id': t.id,
                    'machine_parameter_1': t.machine_parameter_1,
                    'machine_parameter_2': t.machine_parameter_2,
                    'machine_parameter_3': t.machine_parameter_3,
                    'machine_parameter_4': t.machine_parameter_4,
                    'description': t.description,
                    'image': t.image,
                    'virtual_available': t.virtual_available,
                }
                out += json.dumps(o) + ","
            out = out[:-1] + "]"
            return out
        else:
            return "[]"


    @http.route('/machine_management/registerUsage/<data>', auth='user')
    def registerUsage(self, data, **kw):
        print(http.request.params['params'])
        return "{'status':'done'}"

    @http.route('/machine_management/getIdCards/', auth='user')  # , type='http'
    def getIdCards(self, **kw):
        id_cards = http.request.env['lab.id_cards'].search([])
        if not id_cards:
            return "[]"

        out = "["
        for t in id_cards:
            o = {
                'card_id': t.card_id,
                'assigned_client': t.assigned_client.id,
                'status': t.status,
                'card_type': t.card_type,
            }
            out += json.dumps(o) + ","
        out = out[:-1] + "]"
        return out


    @http.route('/machine_management/getCurrentUser', auth='user')  # , type='http'
    def getCurrentuser(self, **kw):
        uid = http.request.env.context.get('uid')
        if not uid:
            return "-1"
        return str(uid)


    @http.route('/machine_management/getUsers/', auth='user')  # , type='http'
    def getUsers(self, **kw):
        users = http.request.env['res.partner'].search([])
        if not users:
            return "[]"

        out = "["
        for t in users:
            if not t.active:
                break
            o = {
                'id': t.id,
                'credit': t.credit,
                'credit_limit': t.credit_limit,
                'name': t.name,
            }
            out += json.dumps(o) + ","
        out = out[:-1] + "]"
        return out


    @http.route('/machine_management/getMachine/<int:machine_id>', auth='user')  # , type='http'
    def getMachine(self, machine_id, **kw):
        m = http.request.env['lab.machine'].search([('id', '=', machine_id)])
        if len(m) != 1:
            return "[]"
        user_ids = [x['id'] for x in m.user_ids]
        owner_ids = [x['id'] for x in m.owner_ids]
        machine_info = {
            'name': m.name,
            'status': m.status,
            'rules': m.rules,
            'user_ids': user_ids,
            'owner_ids': owner_ids,
            'machine_tag_1': m.machine_tag_1.id,
            'machine_tag_2': m.machine_tag_2.id,
        }
        return json.dumps(machine_info)

    @http.route('/machine_management/isAccessAllowed/<int:machine_id>/<int:user_id>', auth='public')  # , type='http'
    def index(self, machine_id, user_id, **kw):
        machine = http.request.env['lab.machine'].search([('id', '=', machine_id)])
        if len(machine) != 1:
            return "machine not found"
        if machine['status'] == 'o':
            return "machine is out of order"
        if machine['status'] == 'n':
            return "machine is not ready for use"
        if machine['rules'] == 'f':
            return 'true'
        if machine['rules'] == 'n':
            return "machine access is closed"

        user = http.request.env['res.partner'].search([('id', '=', user_id)])
        if len(user) != 1:
            return "user not found"
        if user in machine['owner_ids']:
            #User is machine owner
            return "true"
        if user in machine['user_ids']:
            #User is machine user
            return "true"

        return "true"



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