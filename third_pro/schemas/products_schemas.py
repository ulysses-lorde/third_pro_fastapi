from pydantic import BaseModel, ConfigDict


class ProductSchema(BaseModel):
    product_name: str
    product_category: str
    product_price: float
    stock: int


class ProductRead(BaseModel):
    id: int
    product_name: str
    product_category: str
    product_price: float
    stock: int
    model_config = ConfigDict(from_attributes=True)


class ProductList(BaseModel):
    products: list[ProductRead]
