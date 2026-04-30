from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from .connection import Base

class PlayerModel(Base):
    __tablename__ = "players"

    account_id: Mapped[str] = mapped_column(String, primary_key=True)
    account_name: Mapped[str] = mapped_column(String)
    kills: Mapped[int] = mapped_column(Integer, default=0)
    deaths: Mapped[int] = mapped_column(Integer, default=0)