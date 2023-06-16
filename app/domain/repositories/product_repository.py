from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.product import Product


class ProductRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Product]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Product:
        pass

    @abstractmethod
    def create(self, product: Product) -> Product:
        pass
