import random
import time


class ColourDistributor:
    """Randomly distributes colours to an LED strip.
    """

    def __init__(self, distribution_duration):
        """Creates a ColourDistribution configuration.

        :param distribution_duration: the time it should take to distribute all
        colours across the LED strip.
        """
        self.distribution_duration = distribution_duration

    def distribute(self, leds, colour_palette):
        """Randomly distributes colours across an LED strip.

        :param leds: the LedStrip object used to communicate with the
        physical LED strip.
        :param colour_palette: the set of colours which should be used to
        distribute
        across the strip.
        :return the state of the colours currently displayed on the LED strip
        in the form of an array.
        """
        strip_data = []
        led_assignment_duration = (
          float(self.distribution_duration) / leds.num_leds)
        initial_colours = [c for c in colour_palette]

        i = 0
        while len(initial_colours) > 0:
            colour_index = random.randint(0, len(initial_colours) - 1)
            _assign_random_colour(
              leds,
              strip_data,
              i,
              initial_colours,
              colour_index,
              led_assignment_duration)
            initial_colours.pop(colour_index)
            i += 1

        for i in range(i, leds.num_leds):
            colour_index = random.randint(0, len(colour_palette) - 1)
            _assign_random_colour(
              leds,
              strip_data,
              i,
              colour_palette,
              colour_index,
              led_assignment_duration)
        return strip_data


def _assign_random_colour(
  leds,
  strip_data,
  strip_data_index,
  colour_palette,
  colour_index,
  led_assignment_duration):
    colour = colour_palette[colour_index]
    strip_data.append(colour)
    leds.set_colour_and_display(colour, strip_data_index)
    time.sleep(led_assignment_duration)
