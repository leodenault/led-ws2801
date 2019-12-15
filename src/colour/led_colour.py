"""Utility class for holding multi-channel colour data.
"""


class Colour:
    def __init__(self, r, g, b, name=""):
        """Creates a Colour object for holding data on the red, green,
        and blue colour channels.

        :param r: the red component of the colour, expressed as a number
        between 0 and 255.
        :param g: the green component of the colour, expressed as a number
        between 0 and 255.
        :param b:  the blue component of the colour, expressed as a number
        between 0 and 255.
        :param name: the name of the colour.
        """
        self.r = max(0, min(r, 255))
        self.g = max(0, min(g, 255))
        self.b = max(0, min(b, 255))
        self.name = name

    def add(self, other):
        """Returns a new Colour whose components are the sum of other's
        and this one's.
        """
        return Colour(self.r + other.r, self.g + other.g, self.b + other.b)

    def multiply(self, factor):
        """Returns a Colour whose components are the product of factor and
        this Colour's components.
        """
        return Colour(
          int(self.r * factor),
          int(self.g * factor),
          int(self.b * factor))

    def copy(self):
        """Returns a copy of this colour.
        """
        return Colour(self.r, self.g, self.b)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return "({0}, {1}, {2})".format(self.r, self.g, self.b)


WHITE = Colour(255, 255, 255, "White")
RED = Colour(255, 0, 0, "Red")
DARK_RED = Colour(50, 0, 0, "Dark Red")
GREEN = Colour(0, 255, 0, "Green")
DARK_GREEN = Colour(0, 50, 0, "Dark Green")
BLUE = Colour(0, 0, 255, "Blue")
DARK_BLUE = Colour(0, 0, 80, "Dark Blue")
BLACK = Colour(0, 0, 0, "Black")
GOLD = Colour(255, 130, 0, "Gold")
PURPLE = Colour(104, 0, 204, "Purple")
CYAN = Colour(0, 184, 230, "Cyan")
TWINKLE_GOLD = Colour(255, 140, 30, "Off-White")
