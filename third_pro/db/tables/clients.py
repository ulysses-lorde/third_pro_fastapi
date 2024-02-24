from sqlalchemy import CHAR, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from third_pro.configs.base import Base


class Client(Base):
    __tablename__ = 'clients'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    cpf: Mapped[int] = mapped_column(CHAR(14), nullable=False)
