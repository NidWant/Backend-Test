from fastapi import APIRouter
from app.api.route_handler.product_route_handler import router as product_routes

router = APIRouter()

router.include_router(product_routes, prefix="/products", tags=["products"])
