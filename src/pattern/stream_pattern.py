import time

from pattern import Pattern
import math


def create_colour_cycle(base_colours, total_colours):
    """Creates a list of colours which cycles through the base set of colours.

    :param base_colours: the base set of colours which will be repeated in
    the returned list of colours.
    :param total_colours: the total number of colours which should appear in
    the returned list of colours.
    :return: a list of colours containing the set of colours in base_colours
    repeated cyclically.
    """
    return [
        base_colours[i % len(base_colours)] for i in range(0, total_colours)]


class StreamPattern(Pattern):
    """Displays a pattern which moves a set of colours in a single direction
    continuously.

    These colours are placed equidistant from each other and the LEDs between
    them are interpolated.
    """

    def __init__(self, duration, leds_per_second, interpolation_mode):
        """Creates a StreamPattern object.

        :param duration: the amount of time to display the pattern.
        :param leds_per_second: the amount, in LED pixels, by which to move
        the position of the colours every second
        :param interpolation_mode: the InterpolationMode to use to
        interpolate between two colours on the LED strip.
        """
        self.duration = duration
        self.leds_per_second = leds_per_second
        self.interpolation_mode = interpolation_mode

    def animate(self, leds, colour_palette):
        super(StreamPattern, self).animate(leds, colour_palette)
        num_colours = len(colour_palette)
        num_leds = leds.num_leds
        segment_length = float(num_leds) / num_colours
        start_time = time.time()

        time_spent = time.time() - start_time
        while time_spent < self.duration:
            led_offset = time_spent * self.leds_per_second
            for i in range(0, num_colours):
                colour_index = ((i * segment_length) + led_offset) % num_leds
                for j in range(0, int(segment_length)):
                    intermediate_led_index = int(math.ceil(
                      (colour_index + j)) % num_leds)
                    distance = intermediate_led_index - colour_index
                    if distance < 0:
                        distance = num_leds + distance
                    interpolated_colour = self.interpolation_mode.interpolate(
                      colour_palette[i],
                      colour_palette[(i + 1) % num_colours],
                      1 - (distance / segment_length))
                    leds.set_colour(interpolated_colour, intermediate_led_index)
            leds.display()
            time_spent = time.time() - start_time
