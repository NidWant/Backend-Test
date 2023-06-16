from typing import List

from sqlalchemy import select

from app.domain.entities.product import Product
from app.domain.repositories.product_repository import ProductRepository
from app.core.error import AppException, Kind
from app.infrastructure.db.database import SessionLocal
from app.infrastructure.db.mappers import ProductMapper
from app.infrastructure.db.models import ProductModel
from sqlalchemy.orm import Session
from app.core.logger import logger


class SQLProductRepository(ProductRepository):
    def __init__(self, db: Session = SessionLocal()):
        self.db = db

    def get_all(self) -> List[Product]:
        products_model = self.db.execute(select(ProductModel)).scalars().all()
        return [ProductMapper.to_domain_model(product) for product in products_model]

    def get_by_id(self, id: int) -> Product:
        product_model = self.db.get(ProductModel, id)
        if product_model is None:
            details: dict = {"params": "Product with id {} not found".format(id)}
            raise AppException(kind=Kind.NotFound, location="database.product",
                               message="Product with this id not found", code="product_not_found", details=details)

        return ProductMapper.to_domain_model(product_model)

    def create(self, product: Product) -> Product:
        product_model = ProductMapper.to_database_model(product)
        self.db.add(product_model)
        self.db.commit()
        self.db.refresh(product_model)
        logger.info("Product with id {} created.".format(product_model.id))
        return ProductMapper.to_domain_model(product_model)
