from typing import Dict

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards.builders.reply.reply_builder import start_keyboard

from dependency_injector.wiring import inject, Provide

from entities.databases.postgres.services.user_service import UserService
from entities.databases.redis.services.service import Service

from entities.containers.database.postgres_container import PostgresContainer
from entities.containers.database.redis_container import UserRedisContainer


router = Router()

@router.message(CommandStart())
async def start_up(message: Message, information: Dict):
    message_text = await message.answer(
            f"Hello, {message.from_user.full_name}!", 
            reply_markup = start_keyboard(
                ['Profile', 'Tasks']
            )
        )
    return message_text


@router.message(F.text.lower() == "profile")
async def profile(message: Message, information: Dict):
    return await message.answer(f"{information}")
    
    




