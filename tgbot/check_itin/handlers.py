from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

from tgbot.check_itin.static_text import seems_you_didnt_select_itin_type, type_your_itin, \
    cancel_typing_response, try_one_more_time
from tgbot.check_itin.utils import CheckITIN
from tgbot.lang_utils import get_user_lang_from_update, get_text_for_user
from tgbot.onboarding.keyboards import choose_itin_types_keyboard, cancel_typing_itin

RECEIVE_ITIN_AND_CHECK_IT, = range(1)


def select_itin_type_handler(update: Update, context: CallbackContext) -> int:
    selected_ITIN_type = update.message.text
    context.user_data['selected_type'] = selected_ITIN_type

    update.message.reply_text(
        text=get_text_for_user(type_your_itin, update),
        reply_markup=cancel_typing_itin(update)
    )

    return RECEIVE_ITIN_AND_CHECK_IT


def check_itin_handler(update: Update, context: CallbackContext) -> None:
    selected_ITIN_type = context.user_data.get('selected_type')
    if selected_ITIN_type is None:
        update.message.reply_text(
            text=get_text_for_user(seems_you_didnt_select_itin_type, update),
            reply_markup=choose_itin_types_keyboard(update)
        )
        return ConversationHandler.END

    possible_itin = update.message.text

    user_lang = get_user_lang_from_update(update)
    checking_itin = CheckITIN(possible_itin, selected_ITIN_type, user_lang)
    valid, response_text = checking_itin.check()
    if valid:
        update.message.reply_text(
            text=response_text,
            reply_markup=choose_itin_types_keyboard(update),
        )
        return ConversationHandler.END
    else:
        one_more_time_text = get_text_for_user(try_one_more_time, update)
        text = f"{response_text}\n{one_more_time_text}"
        update.message.reply_text(text=text)
        return RECEIVE_ITIN_AND_CHECK_IT


def cancel_typing_handler(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        text=get_text_for_user(cancel_typing_response, update),
        reply_markup=choose_itin_types_keyboard(update),
    )
    return ConversationHandler.END
