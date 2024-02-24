from typing import Optional

from third_pro.configs.connection import DBConnectionHandler
from third_pro.db.tables.products import Product
from third_pro.schemas.products_schemas import (
    ProductList,
    ProductRead,
    ProductSchema,
)

# from sqlalchemy.exc import NoResultFound
# from sqlalchemy import select


class ProductsRepository:
    def __init__(self):
        self.db_handler = DBConnectionHandler()

    def insert(self, product: ProductSchema) -> ProductRead:
        with self.db_handler as db:
            try:
                data_insert = Product(
                    product_name=product.product_name,
                    product_category=product.product_category,
                    product_price=product.product_price,
                    stock=product.stock,
                )
                db.session.add(data_insert)
                db.session.commit()
                db.session.refresh(data_insert)

                return ProductRead(**data_insert.__dict__)

            except Exception as exception:
                db.session.rollback()
                raise exception

    def select_all(self, offset: int, limit: int) -> Optional[ProductList]:
        with self.db_handler as db:
            try:
                products = (
                    db.session.query(Product).offset(offset).limit(limit).all()
                )
                return ProductList(products=products)

            except Exception as exception:
                db.session.rollback()
                raise exception

    """def select_product_category(self, category):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Product).filter(Product.product_category == category).one()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception



    def update(self,):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Product).filter(Product == ).update({ "ano": ano })
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
"""

    def delete(self, product_id):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Product).filter(
                    Product.id == product_id
                ).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
