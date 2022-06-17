from telegram.ext import ConversationHandler, MessageHandler, Filters, CommandHandler

from tgbot.check_itin.handlers import select_itin_type_handler, RECEIVE_ITIN_AND_CHECK_IT, check_itin_handler, \
    cancel_typing_handler
from tgbot.check_itin.static_text import ITIN_CHOICE_REXEXP, cancel_typing_regex

checking_itin_conv_handler = ConversationHandler(
    entry_points=[
        MessageHandler(Filters.regex(ITIN_CHOICE_REXEXP), select_itin_type_handler)
    ],
    states={
        RECEIVE_ITIN_AND_CHECK_IT: [
            MessageHandler(Filters.regex(f"^(?!.*({cancel_typing_regex})).*"), check_itin_handler)
        ],
    },
    fallbacks=[
        CommandHandler("cancel", cancel_typing_handler),
        MessageHandler(
            Filters.regex(cancel_typing_regex), cancel_typing_handler
        ),
    ],
)
