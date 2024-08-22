from typing import Dict

from datetime import datetime

from sqlalchemy import select, delete, update, insert
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from entities.databases.postgres.models.user_model import User



class UserRepository:

    def __init__(self, session: AsyncSession) -> None:
        self.session_factory: AsyncSession = session


    async def create_user(self, data: Dict) -> Dict:
        async with self.session_factory() as session:
            await session.execute(
                insert(User)
                .values(
                    data
                )
            )
            await session.commit()

    
    async def get_user(self, telegram_id: int) -> Dict:
        async with self.session_factory() as session:
            query = await session.execute(
                select(User).where(User.telegram_id == telegram_id)
            )
            result = query.scalars().first()
            if result:
                return result.as_dict()
            return dict()
            