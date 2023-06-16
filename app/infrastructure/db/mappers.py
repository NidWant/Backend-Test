from app.domain.entities.product import Product
from app.infrastructure.db.models import ProductModel


class ProductMapper:
    @staticmethod
    def to_domain_model(product_model: ProductModel) -> Product:
        return Product(
            id=product_model.id,
            name=product_model.name,
            price=product_model.price,
            category=product_model.category
        )

    @staticmethod
    def to_database_model(product: Product) -> ProductModel:
        return ProductModel(
            name=product.name,
            price=product.price,
            category=product.category
        )
