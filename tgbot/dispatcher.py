import logging
import sys

import telegram
from telegram import Bot, BotCommand, Update
from telegram.ext import CommandHandler, Dispatcher, MessageHandler, Filters

from config import TELEGRAM_TOKEN
from tgbot.check_itin.dispatcher import checking_itin_conv_handler
from tgbot.check_itin.static_text import ITIN_CHOICE_REXEXP
from tgbot.onboarding import handlers as onboarding_handlers
from tgbot.check_itin import handlers as checking_itin_handlers


def setup_dispatcher(dp):
    """
    Adding handlers for events from Telegram
    """
    # onboarding
    dp.add_handler(CommandHandler("start", onboarding_handlers.command_start))
    dp.add_handler(checking_itin_conv_handler)

    return dp


def set_up_commands(bot_instance: Bot) -> None:
    langs_with_commands: dict[str, dict[str, str]] = {
        'en': {
            'start': 'Start Phystech.Centre bot 🚀',
        },
        'ru': {
            'start': 'Запустить бота Физтех.Центра 🚀',
        }
    }

    bot_instance.delete_my_commands()
    for language_code in langs_with_commands:
        bot_instance.set_my_commands(
            language_code=language_code,
            commands=[
                BotCommand(command, description) for command, description in langs_with_commands[language_code].items()
            ]
        )


bot = Bot(TELEGRAM_TOKEN)
try:
    TELEGRAM_BOT_USERNAME = bot.get_me()["username"]
except telegram.error.Unauthorized:
    logging.error(f"Invalid TELEGRAM_TOKEN.")
    sys.exit(1)


set_up_commands(bot)
dispatcher = setup_dispatcher(Dispatcher(bot, update_queue=None, workers=4, use_context=True))


def process_telegram_event(update_json, bot):
    update = Update.de_json(update_json, bot)
    dispatcher.process_update(update)
