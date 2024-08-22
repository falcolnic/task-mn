from typing import List

from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def start_keyboard(buttons: List) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    for button in buttons:
        builder.add(KeyboardButton(text = button))
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)