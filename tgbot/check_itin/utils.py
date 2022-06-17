from typing import Tuple, Optional

from tgbot.check_itin.manage_data import ITIN_TYPE_LEGAL, ITIN_TYPE_INDIVIDUAL
from tgbot.check_itin.static_text import itin_must_be_number, legal_entity_must_be_10_digits, \
    individual_must_be_12_digits, not_valid_ITIN, valid_ITIN, ITIN_INDIVIDUAL, ITIN_TYPE_LEGAL_ENTITY
from tgbot.lang_utils import get_text_for_user_lang


class CheckITIN:
    def __init__(self, possible_itin: str, selected_itin_type, user_lang: str):
        self.possible_itin = possible_itin
        self.selected_itin_type = selected_itin_type
        self.user_lang = user_lang

    def _check_legal_entity(self) -> Tuple[bool, Optional[str]]:
        if len(self.possible_itin) != 10:
            return False, get_text_for_user_lang(legal_entity_must_be_10_digits, self.user_lang)

        control_digit = int(self.possible_itin[-1])
        magic_sum = 2*int(self.possible_itin[0]) +\
                    4*int(self.possible_itin[1]) + \
                    10*int(self.possible_itin[2]) + \
                    3*int(self.possible_itin[3]) + \
                    5*int(self.possible_itin[4]) + \
                    9*int(self.possible_itin[5]) + \
                    4*int(self.possible_itin[6]) + \
                    6*int(self.possible_itin[7]) + \
                    8*int(self.possible_itin[8])
        if control_digit != (magic_sum % 11) % 10:
            return False, get_text_for_user_lang(not_valid_ITIN, self.user_lang)
        return True, get_text_for_user_lang(valid_ITIN, self.user_lang)

    def _check_individual(self) -> Tuple[bool, Optional[str]]:
        if len(self.possible_itin) != 12:
            return False, get_text_for_user_lang(individual_must_be_12_digits, self.user_lang)

        first_control_digit = int(self.possible_itin[-2])
        second_control_digit = int(self.possible_itin[-1])
        first_magic_sum = 7*int(self.possible_itin[0]) +\
                          2*int(self.possible_itin[1]) + \
                          4*int(self.possible_itin[2]) + \
                          10*int(self.possible_itin[3]) + \
                          3*int(self.possible_itin[4]) + \
                          5*int(self.possible_itin[5]) + \
                          9*int(self.possible_itin[6]) + \
                          4*int(self.possible_itin[7]) + \
                          6*int(self.possible_itin[8]) + \
                          8*int(self.possible_itin[9])
        second_magic_sum = 3*int(self.possible_itin[0]) +\
                           7*int(self.possible_itin[1]) + \
                           2*int(self.possible_itin[2]) + \
                           4*int(self.possible_itin[3]) + \
                           10*int(self.possible_itin[4]) + \
                           3*int(self.possible_itin[5]) + \
                           5*int(self.possible_itin[6]) + \
                           9*int(self.possible_itin[7]) + \
                           4*int(self.possible_itin[8]) + \
                           6*int(self.possible_itin[9]) + \
                           8*int(self.possible_itin[10])

        if any((
            first_control_digit != (first_magic_sum % 11) % 10,
            second_control_digit != (second_magic_sum % 11) % 10,
        )):
            return False, get_text_for_user_lang(not_valid_ITIN, self.user_lang)
        return True, get_text_for_user_lang(valid_ITIN, self.user_lang)

    def check(self) -> Tuple[bool, Optional[str]]:
        if not self.possible_itin.isdigit():
            return False, get_text_for_user_lang(itin_must_be_number, self.user_lang)

        if self.selected_itin_type in ITIN_INDIVIDUAL.values():
            return self._check_individual()
        elif self.selected_itin_type in ITIN_TYPE_LEGAL_ENTITY.values():
            return self._check_legal_entity()
        else:
            raise ValueError(f"Unknown {self.selected_itin_type=}")
