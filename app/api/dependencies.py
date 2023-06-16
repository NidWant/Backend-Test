from fastapi import Depends
from app.domain.repositories.product_repository import ProductRepository
from app.domain.services.product_service import ProductService
from app.infrastructure.db.product_repository import SQLProductRepository


def get_product_repository() -> ProductRepository:
    return SQLProductRepository()


def get_product_service(repository: ProductRepository = Depends(get_product_repository)) -> ProductService:
    return ProductService(repository)
