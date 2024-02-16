from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Float

from third_pro.configs.base import Base


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    product_name: Mapped[str] = mapped_column(String(255), nullable=False)
    product_category: Mapped[str] = mapped_column(String(50), nullable=False)
    product_price: Mapped[float] = mapped_column(Float, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)
    