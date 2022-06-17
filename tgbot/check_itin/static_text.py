ITIN_TYPE_LEGAL_ENTITY = {
    'en': 'Legal entity 🏦',
    'ru': 'Юридическое лицо 🏦',
}
ITIN_INDIVIDUAL = {
    'en': 'Individual 👤',
    'ru': 'Физическое лицо 👤',
}
ITIN_CHOICE_REXEXP = '|'.join(set(ITIN_TYPE_LEGAL_ENTITY.values()).union(set(ITIN_INDIVIDUAL.values())))


choose_itin_type = {
    'en': 'Choose ITIN type 👇',
    'ru': 'Выбери тип ИНН 👇',
}

type_your_itin = {
    'en': 'Please enter your ITIN 👇',
    'ru': 'Введите ИНН 👇',
}

try_one_more_time = {
    'en': 'Try on more time',
    'ru': 'Попробуй еще раз',
}


cancel_typing = {
    'en': 'Cancel ❌',
    'ru': 'Отмена ❌',
}
cancel_typing_regex = '|'.join(cancel_typing.values())


cancel_typing_response = {
    'en': 'Okay, check it next time 👌',
    'ru': 'Ок, проверишь в следующий раз 👌',
}


seems_you_didnt_select_itin_type = {
    'en': "It seems that you haven't chosen ITIN type. Or it was too long time ago. Try again 👇",
    'ru': "Кажется, что вы не выбрали тип ИНН. Или с момента выбора прошло слишком много времени. Попробуй еще раз 👇"
}


itin_must_be_number = {
    'en': 'ITIN must be a number ❌',
    'ru': 'ИНН должно быть числом ❌',
}

legal_entity_must_be_10_digits = {
    'en': 'Legal entity ITIN must contain 10 digits ❌',
    'ru': 'ИНН юридического лица должен состоять из 10 цифр ❌',
}

individual_must_be_12_digits = {
    'en': 'Individual ITIN must contain 12 digits ❌',
    'ru': 'ИНН физического лица должен состоять из 12 цифр ❌',
}

not_valid_ITIN = {
    'en': 'ITIN is not valid ❌',
    'ru': 'ИНН невалиден ❌',
}

valid_ITIN = {
    'en': 'ITIN is valid ✅',
    'ru': 'ИНН валиден ✅',
}


