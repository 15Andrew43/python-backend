from functools import cmp_to_key
from typing import List
from models.product import Product

def get_ordered_products_by_price(products: List[Product]) -> List[Product]:
    return sorted(products, key=cmp_to_key(lambda x, y: y.price - x.price))
