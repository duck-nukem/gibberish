import random

import sys

from colors import CHARACTER_COLORS, Color_Off, BACKGROUND_COLORS

NUMBER_OF_CHARACTERS_TO_PRINT_BY_DEFAULT = 1000


def get_random_character(color, background):
    character = unichr(random.randrange(0x10000))
    return u'{background}{color}{character}{reset}'.format(background=background,
                                                           color=color,
                                                           character=character,
                                                           reset=Color_Off)


def get_colored_character():
    color_index = random.randint(0, len(CHARACTER_COLORS) - 1)
    background_color_index = random.randint(0, len(BACKGROUND_COLORS) - 1)

    color = CHARACTER_COLORS[color_index]
    background_color = BACKGROUND_COLORS[background_color_index]
    return get_random_character(color, background_color)


def get_number_of_characters_to_print():
    try:
        return int(arguments[1] * 1)
    except (IndexError, TypeError):
        return NUMBER_OF_CHARACTERS_TO_PRINT_BY_DEFAULT


if __name__ == '__main__':
    arguments = sys.argv
    to_print = u''
    number_of_characters = get_number_of_characters_to_print()
    for i in range(0, number_of_characters):
        to_print += get_colored_character()
    print(to_print)
