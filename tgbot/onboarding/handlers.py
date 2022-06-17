from telegram import Update
from telegram.ext import CallbackContext

from tgbot.onboarding.keyboards import choose_itin_types_keyboard
from tgbot.onboarding.static_text import hy_this_is_phystech_centre_bot_description
from tgbot.lang_utils import get_text_for_user


def command_start(update: Update, context: CallbackContext) -> None:
    text = get_text_for_user(texts=hy_this_is_phystech_centre_bot_description, update=update)
    markup = choose_itin_types_keyboard(update)

    update.message.reply_text(text=text, reply_markup=markup)
