import random

from colors import Color_Off


class RandomColorizedCharacter(object):
    def __init__(self):
        self.character = RandomColorizedCharacter.get_random_character()

    @staticmethod
    def get_random_character():
        return unichr(random.randint(200, 10000))

    def get_colorized_with(self, background, color):
        return u'\033[0;{background};{color}m{character}{reset}'.format(background=background,
                                                                        color=color,
                                                                        character=self.character,
                                                                        reset=Color_Off)
