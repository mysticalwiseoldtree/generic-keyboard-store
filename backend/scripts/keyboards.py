"""
A keyboard product in store has several properties:
- Name
- Price
- Brand
- Image of the product
- Switch type
"""
class Keyboard:
  def __init__(self, name: str, price: float, brand: str, image: str, switch_type: str):
    self.name = name
    self.price = price
    self.brand = brand
    self.image = image
    self.switch_type = switch_type

# Sample keyboard object
sample_keyboard = Keyboard('Oppressor Mk II', 6000000.69, 'Warstock Cache & Carry', 'https://static.wikia.nocookie.net/gtawiki/images/8/85/OppressorMkII-GTAO-front.png', 'Homing Missiles')
