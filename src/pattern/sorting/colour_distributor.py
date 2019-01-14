import random

from pattern.pattern import Pattern
from pattern.time_interval import TimeInterval


class ColourDistributor(Pattern):
    """Randomly distributes colours to an LED strip.
    """

    def __init__(self, leds, distribution_duration, colour_palette, strip_data):
        """Creates a ColourDistribution pattern.

        This pattern randomly distributes colours from the given colour
        palette on the LED strip.

        :param leds: the LedStrip instance.
        :param distribution_duration: the time it should take to distribute all
        colours across the LED strip.
        :param colour_palette: the palette of colours which will be used to
        randomly distribute colours onto the strip.
        :param strip_data: the colour data displayed on the LED strip before
        beginning this pattern, expressed as an array of Colours.
        """
        self.time_interval = TimeInterval(
          distribution_duration / float(leds.get_num_leds()))
        self.colour_palette = colour_palette
        self.strip_data = strip_data
        self.initial_colours = [c for c in colour_palette]
        self.current_led = 0
        self.num_leds = leds.get_num_leds()

    def update(self, leds, delta):
        time_exceeded = self.time_interval.time_exceeded(delta)
        if self.is_done() or not time_exceeded:
            return

        if len(self.initial_colours) > 0:
            colour_index = self._assign_random_colour(
              leds, self.initial_colours)
            self.initial_colours.pop(colour_index)
        else:
            self._assign_random_colour(leds, self.colour_palette)

        self.current_led += 1

    def is_done(self):
        return self.current_led >= self.num_leds

    def _assign_random_colour(self, leds, colour_palette):
        colour_index = random.randint(0, len(colour_palette) - 1)
        colour = colour_palette[colour_index]
        self.strip_data[self.current_led] = colour
        leds.set_colour(colour, self.current_led)
        return colour_index
