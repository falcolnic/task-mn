from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, MappedColumn
from sqlalchemy import String, Integer, BigInteger, ForeignKey
from sqlalchemy.orm import relationship

from entities.databases.postgres.database import Base

if TYPE_CHECKING:
    from entities.databases.postgres.models.user_model import User


class Task(Base):

    __tablename__ = 'tasks'

    id: Mapped[int] = MappedColumn(Integer, primary_key = True, autoincrement = True)
    user_id: Mapped[int] = MappedColumn(BigInteger, ForeignKey('users.id'), nullable = False)
    title: Mapped[str] = MappedColumn(String, nullable = False)
    description: Mapped[str] = MappedColumn(String, nullable = False)
    status: Mapped[str] = MappedColumn(String, default = 'in progress', nullable = False)
    created: Mapped[str] = MappedColumn(String, nullable = False)

    user: Mapped['User'] = relationship(back_populates = 'tasks', lazy = 'joined')

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}