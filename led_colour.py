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
        self.r = r
        self.g = g
        self.b = b
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

    def __str__(self):
        if self.name:
            return self.name
        else:
            return "({0}, {1}, {2})".format(self.r, self.g, self.b)


Colour.WHITE = Colour(255, 255, 125, "White")
Colour.RED = Colour(150, 0, 0, "Red")
Colour.GREEN = Colour(0, 125, 0, "Green")
Colour.BLUE = Colour(0, 0, 125, "Blue")
Colour.BLACK = Colour(0, 0, 0, "Black")
Colour.GOLD = Colour(255, 125, 0, "Gold")
