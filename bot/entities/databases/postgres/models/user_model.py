from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, MappedColumn
from sqlalchemy import String, Integer, BigInteger, ForeignKey
from sqlalchemy.orm import relationship

from entities.databases.postgres.database import Base

if TYPE_CHECKING:
    from entities.databases.postgres.models.tasks_model import Task


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = MappedColumn(Integer, primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = MappedColumn(BigInteger, nullable=False, unique=True)
    name: Mapped[str] = MappedColumn(String(50), nullable=False)
    joined: Mapped[str] = MappedColumn(String(50), nullable=False)


    tasks: Mapped[list['Task']] = relationship(back_populates='user', lazy = 'joined')

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}