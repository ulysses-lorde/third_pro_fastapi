from typing import Optional

from fastapi import APIRouter, Body, HTTPException, Query, status

from third_pro.db.errors import EntityDoesNotExist, ProductNameAlreadyExists
from third_pro.repository.products_repository import ProductsRepository
from third_pro.schemas.messages import Message
from third_pro.schemas.products_schemas import (
    ProductList,
    ProductRead,
    ProductSchema,
)

router = APIRouter(prefix='/products', tags=['products'])


@router.post(
    '/', response_model=ProductRead, status_code=status.HTTP_201_CREATED
)
def create_product(
    product: ProductSchema = Body(...),
) -> Optional[ProductRead]:
    try:
        repository = ProductsRepository()
        new_product = repository.insert(product=product)
        return new_product

    except ProductNameAlreadyExists:
        raise HTTPException(
            status_code=400, detail='Product Name already registered'
        )


@router.get('/', response_model=ProductList, status_code=status.HTTP_200_OK)
def get_all_products(
    offset: int = Query(default=0),
    limit: int = Query(default=10, lte=100),
) -> Optional[ProductList]:
    repository = ProductsRepository()
    return repository.select_all(offset=offset, limit=limit)


@router.get('/', response_model=ProductList, status_code=status.HTTP_200_OK)
def get_product_by_category():
    pass


@router.delete(
    '/',
    response_model=Message,
)
def delete_product(product_id: int):
    repository = ProductsRepository()
    try:
        repository.delete(product_id)
        return {'detail': 'Product deleted'}

    except EntityDoesNotExist:
        raise HTTPException(status_code=404, detail='Unregistered Product')
