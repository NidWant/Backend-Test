from typing import Optional


class Product:
    def __init__(self, name: str, price: float, category: str, id: Optional[int] = None):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
