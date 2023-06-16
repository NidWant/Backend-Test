from typing import List
from app.domain.entities.product import Product
from app.domain.repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def get_all(self) -> List[Product]:
        return self.repository.get_all()

    def get_by_id(self, id: int) -> Product:
        return self.repository.get_by_id(id)

    def create(self, product: Product) -> Product:
        return self.repository.create(product)
