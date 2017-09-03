#!/usr/bin/env python
import random
import sys

from colors import Color_Off, BACKGROUND_COLORS, CHARACTER_COLORS

NUMBER_OF_CHARACTERS_TO_PRINT_BY_DEFAULT = 1000


def colorize_character(character, color):
    return u'{color}{character}{reset}'.format(color=color, character=character, reset=Color_Off)


def get_random_character():
    return unichr(random.randrange(0x10000))


def get_colored_character():
    color = get_random_color()
    random_character = get_random_character()
    return colorize_character(random_character, color)


def get_random_color():
    background_color_index = get_random_index_from(BACKGROUND_COLORS)
    if background_color_index == 0:
        return get_character_color()
    else:
        return get_background_color(background_color_index)


def get_background_color(background_color_index):
    return BACKGROUND_COLORS[background_color_index]


def get_character_color():
    color_index = get_random_index_from(CHARACTER_COLORS)
    color = CHARACTER_COLORS[color_index]
    return color


def get_random_index_from(array):
    return random.randint(0, len(array) - 1)


def get_number_of_characters_to_print():
    try:
        return int(arguments[1])
    except (IndexError, TypeError):
        return NUMBER_OF_CHARACTERS_TO_PRINT_BY_DEFAULT


def generate_gibberish():
    gibberish_stuff = u''
    for i in range(0, number_of_characters):
        gibberish_stuff += get_colored_character()
    return gibberish_stuff


if __name__ == '__main__':
    arguments = sys.argv
    number_of_characters = get_number_of_characters_to_print()
    gibberish_stuff = generate_gibberish()
    print(gibberish_stuff)
