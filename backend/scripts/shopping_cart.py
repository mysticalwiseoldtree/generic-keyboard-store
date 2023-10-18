"""
The shopping cart. Manages the items in the cart and calculates the total price.
"""

import keyboards


class ShoppingCart:
    def __init__(self):
        self.__items: list[keyboards.UI_Keyboard] = []

    @property
    def total_price(self) -> float:
        sum = 0
        for item in self.__items:
            sum += item.total_price
        return sum

    @property
    def items(self) -> list[keyboards.UI_Keyboard]:
        return self.__items

    def add_item(self, item: keyboards.UI_Keyboard):
        self.__items.append(item)

    def remove_item(self, item: keyboards.UI_Keyboard):
        self.__items.remove(item)
