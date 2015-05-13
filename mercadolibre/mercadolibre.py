# -*- coding: utf-8 -*-

import json
import requests

URL_BASE = 'https://api.mercadolibre.com/sites/MLB/search'

class ConnectionError(Exception):
    pass

class MercadoLibre(object):

    def search_product_by_category(self, category, limit=200, price=None, max_id=None):
        if limit > 0:
            product_list = []
            try:
                response = requests.get(URL_BASE + ('?category=%s&limit=%d&price=%s' % (category, limit, price)))
            except:
                raise ConnectionError('Connection failed!')
            products = json.loads(response.content)
            for product in range(len((products['results']))):
                product_list.append((products['results'][product]['title'], products['results'][product]['price'], products['results'][product]['permalink']))
            return product_list
        return []

    def search_product_by_name(self, name, price=None):
        product_list = []
        try:
            response = requests.get(URL_BASE + ('?q=%s&price=%s') % (name, price))
        except:
            raise ConnectionError('Connection failed!')
        products = json.loads(response.content)
        for product in range(len(products['results'])):
            product_list.append((products['results'][product]['title'], products['results'][product]['price'], products['results'][product]['permalink']))
        return product_list

    def search_product_by_name_in_category(self, name, category, price=None):
        product_list = []
        try:
            response = requests.get(URL_BASE + ('?q=%s&category=%s&price=%s' % (name, category, price)))
        except:
            raise ConnectionError('Connection failed!')
        products = json.loads(response.content)
        for product in range(len(products['results'])):
            product_list.append((products['results'][product]['title'], products['results'][product]['price'], products['results'][product]['permalink']))
            return product_list
