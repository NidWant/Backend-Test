from app.api.presentation.models import ProductIn, ProductOut
from app.domain.entities.product import Product


class ProductMapper:
    @staticmethod
    def to_domain_model(product_in: ProductIn) -> Product:
        return Product(
            name=product_in.name,
            price=product_in.price,
            category=product_in.category
        )

    @staticmethod
    def to_presentation_model(product: Product) -> ProductOut:
        product_dict = {"id": product.id, "name": product.name, "price": product.price, "category": product.category}
        return ProductOut.parse_obj(product_dict)
