from __future__ import print_function
import xmlrpclib
from smartcard.scard import *
import smartcard.util
import pickle
import webbrowser
from bottle import route, run, template, debug

static

@route('/local_pos/categories')
def generate_categories():
    print(Access().categories)
    return template('templates/make_categories', data=Access().categories)

Access():
    url = 'http://127.0.0.1:8069'
    db = 'FabLabKA'
    username = 'admin'
    password = 'admin'

    _common = None
    _uid = None
    _models = None
    customers = None
    products = None
    categories = None

    def start_bottle(self):
        debug(True)
        run(reloader=True)

    def main(self):
        self.init()

        try:
            #webbrowser.open_new_tab("file:///home/pcaroli/odoo_addons/local_pos/static/index.html")
            pass
        except:
            print("Cannot open Webbrowser!")
        #run(host='localhost', port=8080)
        self.start_bottle()


    def init(self):
        try:
            self._common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
            print(self._common.version())
            self._uid = self._common.authenticate(self.db, self.username, self.password, {})
            self._models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(self.url))

            self.customers = self._models.execute_kw(self.db, self._uid, self.password,
                                    'res.partner', 'search_read',
                                    [[['customer', '=', 'true']]])
            self.products = self._models.execute_kw(self.db, self._uid, self.password,
                                    'product.product', 'search_read',
                                    [[['sale_ok', '=', True]]])
            self.categories = self._models.execute_kw(self.db, self._uid, self.password,
                                    'product.category', 'search_read',
                                    [])
            print("CUSTOMERS")
            for i in self.customers:
                print( i['name'] + ",  ", end="")
            print("\nPRODUCTS")
            for i in self.products:
                print( i['name'] + ",  ", end="")
            print("\nCATEGORIES")
            for i in self.categories:
                print( i['name'] + ",  ", end="")
            print("")
            pickle.dump(self.customers, open("customers.db", "wb"))
            pickle.dump(self.products, open("products.db", "wb"))
            pickle.dump(self.categories, open("categories.db", "wb"))

            print("BACKUP_DB_SAVED")

        except IOError:
            print("COULD_NOT_OPEN_CONNECTION")
            try:
                print("BACKUP_DB_LOADED")
                self.customers = pickle.load(open("customers.db", "rb"))
                self.products = pickle.load(open("products.db", "rb"))
                self.categories = pickle.load(open("categories.db", "rb"))
            except ValueError:
                print("COULD_NOT_LOAD_BACKUP_DB")


    def get_access_rfid(self):
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
                    return self.check_access(current_card)
                else:
                    print("NO_CARD")
            else:
                print("NO_READER")
        else:
            print("FAILED")

if __name__ == "__main__":
    Access().main()


