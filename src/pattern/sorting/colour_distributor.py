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
        led_assignment_duration = self.distribution_duration / leds.num_leds
        for i in range(0, leds.num_leds):
            colour = colour_palette[random.randint(0, len(colour_palette) - 1)]
            strip_data.append(colour)
            leds.set_colour_and_display(colour, i)
            time.sleep(led_assignment_duration)
        return strip_data
