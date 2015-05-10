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
from mercado_libre.mercado_libre import MercadoLibre

mercado = MercadoLibre()

mercado.search_product_by_name_in_category('dvd', 'MLB1648', '1-1000')
```
