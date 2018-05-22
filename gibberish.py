#!/usr/bin/env python
import random
import sys

from RandomColorizedCharacter import RandomColorizedCharacter
from colors import BACKGROUND_COLORS, CHARACTER_COLORS

NUMBER_OF_CHARACTERS_TO_PRINT_BY_DEFAULT = 1000


def get_colored_character():
    background = get_random_color_from(BACKGROUND_COLORS)
    color = get_random_color_from(CHARACTER_COLORS)
    return RandomColorizedCharacter().get_colorized_with(background, color)


def get_random_color_from(array):
    return str(array[get_random_index_from(array)])


def get_random_index_from(array):
    return random.randint(0, len(array) - 1)


def get_number_of_characters_to_print(arguments):
    try:
        return int(arguments[1])
    except (IndexError, TypeError):
        return NUMBER_OF_CHARACTERS_TO_PRINT_BY_DEFAULT


def generate_gibberish():
    gibberish_stuff = u''
    for _ in range(0, number_of_characters):
        gibberish_stuff += get_colored_character()
    return gibberish_stuff


if __name__ == '__main__':
    arguments = sys.argv
    number_of_characters = get_number_of_characters_to_print(arguments)
    gibberish_stuff = generate_gibberish()
    print(gibberish_stuff)
