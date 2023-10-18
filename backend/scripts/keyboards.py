"""
Keyboard product class and its shopping cart variant
"""

# A keyboard product in store has several properties:
# - Name
# - Price
# - Brand
# - Image of the product
# - Switch type


class Keyboard:
    def __init__(
        self, name: str, price: float, brand: str, image: str, switch_type: str
    ):
        self.name = name
        self.price = price
        self.brand = brand
        self.image = image
        self.switch_type = switch_type


# Sample keyboard object
sample_keyboard = Keyboard(
    "Oppressor Mk II",
    6000000.69,
    "Warstock Cache & Carry",
    "https://static.wikia.nocookie.net/gtawiki/images/8/85/OppressorMkII-GTAO-front.png",
    "Homing Missiles",
)

# A UI_Keyboard is a keyboard product in the shopping cart.
# It has the same properties as a keyboard product in store,
# but it also has two additional properties:
# - Quantity
# - Total price (price * quantity)


class UI_Keyboard(Keyboard):
    def __init__(self, keyboard: Keyboard):
        self.product = Keyboard(
            keyboard.name,
            keyboard.price,
            keyboard.brand,
            keyboard.image,
            keyboard.switch_type,
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
