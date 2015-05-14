# API Mercado Libre

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
- name: String representing something to search.
- category: String representing a category.
- price: String representing a price range.

### Search product by name

### Search product by name in category

#To do
-
