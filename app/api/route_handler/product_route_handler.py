from fastapi import APIRouter, Depends, status
from typing import List

from app.domain.services.product_service import ProductService
from app.api.dependencies import get_product_service
from app.api.presentation.mappers import ProductMapper
from app.api.presentation.models import ProductOut, ProductIn

router = APIRouter()


@router.get("/", response_model=List[ProductOut])
def get_all_products(service: ProductService = Depends(get_product_service)):
    products = service.get_all()
    return [ProductMapper.to_presentation_model(product) for product in products]


@router.get("/{id}", response_model=ProductOut)
def get_product_by_id(id: int, service: ProductService = Depends(get_product_service)):
    product_domain = service.get_by_id(id)
    product_presentation = ProductMapper.to_presentation_model(product_domain)
    return product_presentation


@router.post("/", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductIn, service: ProductService = Depends(get_product_service)):
    product_domain = ProductMapper.to_domain_model(product)
    product_presentation = ProductMapper.to_presentation_model(service.create(product_domain))
    return product_presentation
