from typing import Dict

from entities.databases.postgres.repositories.user_repository import UserRepository


class UserService:

    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository: UserRepository = user_repository


    async def create_user(self,data: Dict) -> Dict:
        user = await self.user_repository.create_user(
            data = data
        )

        return user
    

    async def get_user(self, telegram_id: int) ->Dict:
        user = await self.user_repository.get_user(
            telegram_id = telegram_id
        )

        return user