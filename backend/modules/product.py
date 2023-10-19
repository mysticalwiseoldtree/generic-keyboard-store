"""
Product class and its shopping cart variant
"""

from uuid import uuid4


class Product:
    """
    A product in store has several properties:
    - Name
    - Price
    - Category
    - Image of the product
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        category: str,
        image: str,
        __unique_product_id: str = "",
    ):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.image = image
        self.unique_product_id = (
            __unique_product_id if __unique_product_id != "" else uuid4().hex
        )


# Sample product object
sample_product = Product(
    "Oppressor Mk II",
    "Bike that goes in the air and fire homing missiles",
    6000000.69,
    "Warstock Cache & Carry",
    "https://static.wikia.nocookie.net/gtawiki/images/8/85/OppressorMkII-GTAO-front.png",
)


class UI_Product(Product):
    """
    A UI_Product is a product in the shopping cart.
    It has the same properties as a product in store,
    but it also has two additional properties:
    - Quantity
    - Total price (price * quantity)
    """

    def __init__(self, product: Product):
        self.product = Product(
            product.name,
            product.description,
            product.price,
            product.category,
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
