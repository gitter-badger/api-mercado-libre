# API Mercado Libre

[![Join the chat at https://gitter.im/hudsonbrendon/api-mercado-libre](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/hudsonbrendon/api-mercado-libre?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

![Mercado Libre](mercado-libre.jpg)

Simple integrate of API mercado libre with python

# Quick start

```bash
$ pip install mercado-libre
```
or

```bash
$ python setup.py install
```
# Usage

```python
from mercadolibre.mercadolibre import MercadoLibre

mercado = MercadoLibre()

mercado.search_product_by_name_in_category('dvd', 'MLB1648', '1-1000')
```
# Commands available


### Search product by category

MercadoLibre.search_product_by_category(category, limit=200, price=None)

Return a list of tuple with format (product_name, price, url).

args:
- category: String representing category to search.
- limit: integer representing an amount.
- price: String representing a price range.

### Search product by name

MercadoLibre.search_product_by_name(name, limit=200, price=None)

Return a list of tuple with format (name, price, url).

args:
- name: String representing something to search.
- limit: integer representing an amount.
- price: String representing a price range.

### Search product by name in category

MercadoLibre.search_product_by_name_in_category(name, limit=200, price=None)

Return a list of tuple with format (product_name, price, url).

args:
- name: String representing something to search.
- limit: integer representing an amount.
- price: String representing a price range.

# Dependencies

- Python 2.7
- [requests](http://docs.python-requests.org/en/latest/)

#To do
-
