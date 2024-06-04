

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from injection.app.database.postgres import Base


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(30), index=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, index=False)
    