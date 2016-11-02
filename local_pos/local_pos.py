from __future__ import print_function
import xmlrpclib
from smartcard.scard import *
import smartcard.util
import pickle
import webbrowser
import time
from bottle import route, run, template, debug


url = 'http://127.0.0.1:8069'
db = 'FabLabKA'
username = 'admin'
password = 'admin'

_common = None
_uid = None
_models = None
odoo_customers = 0
odoo_products = 0
odoo_categories = 0


def start_bottle():
    debug(True)
    run(reloader=True)


def main():
    init()
    try:
        #webbrowser.open_new_tab("file:///home/pcaroli/odoo_addons/local_pos/static/index.html")
        pass
    except:
        print("Cannot open Webbrowser!")
    #run(host='localhost', port=8080)
    time.sleep(2)
    start_bottle()


def init():
    try:
        _common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
        print(_common.version())
        _uid = _common.authenticate(db, username, password, {})
        _models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
        global odoo_customers
        odoo_customers = _models.execute_kw(db, _uid, password,
                                'res.partner', 'search_read',
                                [[['customer', '=', 'true']]])
        global odoo_products
        odoo_products = _models.execute_kw(db, _uid, password,
                                'product.product', 'search_read',
                                [[['sale_ok', '=', True]]])
        global odoo_categories
        odoo_categories = _models.execute_kw(db, _uid, password,
                                'product.category', 'search_read',
                                [])
        print("CUSTOMERS")
        for i in odoo_customers:
            print( i['name'] + ",  ", end="")
        print("\nPRODUCTS")
        for i in odoo_products:
            print( i['name'] + ",  ", end="")
        print("\nCATEGORIES")
        for i in odoo_categories:
            print( i['name'] + ",  ", end="")
        print("")
        pickle.dump(odoo_customers, open("customers.db", "wb"))
        pickle.dump(odoo_products, open("products.db", "wb"))
        pickle.dump(odoo_categories, open("categories.db", "wb"))

        print("BACKUP_DB_SAVED")

    except IOError:
        print("COULD_NOT_OPEN_CONNECTION")
        try:
            print("BACKUP_DB_LOADED")
            odoo_customers = pickle.load(open("customers.db", "rb"))
            odoo_products = pickle.load(open("products.db", "rb"))
            odoo_categories = pickle.load(open("categories.db", "rb"))
        except ValueError:
            print("COULD_NOT_LOAD_BACKUP_DB")


def get_access_rfid():
    hresult, hcontext = SCardEstablishContext(SCARD_SCOPE_USER)
    if hresult == SCARD_S_SUCCESS:
        hresult, readers = SCardListReaders(hcontext, [])
        if len(readers) > 0:
            reader = readers[0]
            hresult, hcard, dwActiveProtocol = SCardConnect(
            hcontext,
            reader,
            SCARD_SHARE_SHARED,
            SCARD_PROTOCOL_T0 | SCARD_PROTOCOL_T1)
            if hresult == 0:
                hresult, response = SCardTransmit(hcard,dwActiveProtocol,[0xFF,0xCA,0x00,0x00,0x00])
                current_card = smartcard.util.toHexString(response)
                print(current_card)
                return check_access(current_card)
            else:
                print("NO_CARD")
        else:
            print("NO_READER")
    else:
        print("FAILED")


@route('/local_pos/categories')
def generate_categories():
    print(odoo_categories)
    #awesome, bottle doesn't support "non-hashable" items...
    #return template('templates/make_categories', data=odoo_categories)
    ret = "<div class='container'>"
    ret += "<div class='row'>"
    for item in odoo_categories:
        ret += "<div class=/'col-sm-2/'>"
        ret += "    " + item['name']
        ret += "</div>"
    ret += "</div>"
    ret += "</div>"
    return ret

if __name__ == "__main__":
    main()


