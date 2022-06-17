from enum import Enum

from telegram import Update


class UserLang(Enum):
    english = 'en'
    russian = 'ru'


def get_user_lang_from_update(update: Update) -> str:
    lang_code = update.effective_user.language_code
    if lang_code == UserLang.russian:
        lang = UserLang.russian
    elif lang_code == UserLang.english:
        lang = UserLang.english
    else:
        lang = UserLang.english
    return lang.value


def get_text_for_user_lang(texts: dict[str, str], user_lang: str) -> str:
    text_by_lang = texts.get(user_lang)
    if text_by_lang:
        return text_by_lang
    return texts[user_lang]


def get_text_for_user(texts: dict[str, str], update: Update) -> str:
    user_lang = get_user_lang_from_update(update)
    return get_text_for_user_lang(texts, user_lang)
