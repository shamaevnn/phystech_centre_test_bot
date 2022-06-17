from telegram import ReplyKeyboardMarkup, KeyboardButton, Update

from tgbot.check_itin.static_text import ITIN_TYPE_LEGAL_ENTITY, ITIN_INDIVIDUAL, cancel_typing
from tgbot.lang_utils import get_text_for_user


def choose_itin_types_keyboard(update: Update) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(
                text=get_text_for_user(texts=ITIN_TYPE_LEGAL_ENTITY, update=update),
            )],
            [KeyboardButton(
                text=get_text_for_user(texts=ITIN_INDIVIDUAL, update=update)
            )]
        ],
        resize_keyboard=True
    )


def cancel_typing_itin(update: Update) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [[KeyboardButton(text=get_text_for_user(texts=cancel_typing, update=update))]],
        resize_keyboard=True
    )
