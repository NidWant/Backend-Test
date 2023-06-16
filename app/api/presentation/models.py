from pydantic import BaseModel


class ProductIn(BaseModel):
    name: str
    price: float
    category: str


class ProductOut(ProductIn):
    id: int
