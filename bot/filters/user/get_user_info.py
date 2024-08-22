from typing import Union, Dict, Any, Annotated

from aiogram.filters import BaseFilter
from aiogram.types import Message

from datetime import datetime

from dependency_injector.wiring import Provide, inject

from entities.databases.postgres.services.user_service import UserService
from entities.databases.redis.services.service import Service

from entities.containers.database.postgres_container import PostgresContainer
from entities.containers.database.redis_container import UserRedisContainer


class UserInfoFilter(BaseFilter):

    def __init__(
        self, db: Annotated[UserService, Provide[PostgresContainer.user_service]],
        user_redis: Annotated[Service, Provide[UserRedisContainer.redis_service]]
    ) -> None:
        self.db: UserService = db
        self.user_redis: user_redis = user_redis
       
    
    async def __call__(self, message: Message) -> Union[bool, Dict[str, Any]]:
        data = dict(
            telegram_id = message.from_user.id, 
            name = message.from_user.full_name,
            joined = str(datetime.now())
        )
        if not await self.user_redis.getItem(key = message.from_user.id):
            await self.user_redis.CreateItem(key = message.from_user.id, value = data)
        else:
            return {"information": data}
        if not await self.db.get_user(telegram_id = message.from_user.id):
            await self.db.create_user(data = data)
        return {"information": data}