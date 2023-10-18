"""
Product class and its shopping cart variant
"""

from uuid import uuid4

# A product in store has several properties:
# - Name
# - Price
# - Brand
# - Image of the product


class Product:
    def __init__(
        self,
        name: str,
        price: float,
        brand: str,
        image: str,
        __uniqueid: str = "",
    ):
        self.name = name
        self.price = price
        self.brand = brand
        self.image = image
        self.uniqueid = __uniqueid if __uniqueid != "" else uuid4().hex


# Sample product object
sample_product = Product(
    "Oppressor Mk II",
    6000000.69,
    "Warstock Cache & Carry",
    "https://static.wikia.nocookie.net/gtawiki/images/8/85/OppressorMkII-GTAO-front.png",
)

# A UI_Product is a product product in the shopping cart.
# It has the same properties as a product product in store,
# but it also has two additional properties:
# - Quantity
# - Total price (price * quantity)


class UI_Product(Product):
    def __init__(self, product: Product):
        self.product = Product(
            product.name,
            product.price,
            product.brand,
            product.image,
        )
        self.__quantity: int = 0

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, new_value: int):
        if new_value >= 0:
            self.__quantity = new_value

    @property
    def total_price(self) -> float:
        return self.product.price * self.quantity

    def isSelected(self) -> bool:
        return self.quantity > 0
