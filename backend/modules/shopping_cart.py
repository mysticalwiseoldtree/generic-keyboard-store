"""
The shopping cart. Manages the items in the cart and calculates the total price.
"""

import backend.modules.product as product


class ShoppingCart:
    def __init__(self, cart_items: list[product.UI_Product] = []):
        self.__items: list[product.UI_Product] = cart_items

    @property
    def total_price(self) -> float:
        sum = 0
        for item in self.__items:
            sum += item.total_price
        return sum

    @property
    def items(self) -> list[product.UI_Product]:
        return self.__items

    def add_item(self, item: product.UI_Product):
        self.__items.append(item)

    def remove_item(self, item: product.UI_Product):
        self.__items.remove(item)
