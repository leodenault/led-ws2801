import math

from timed_pattern import TimedPattern


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


class StreamPattern(TimedPattern):
    """Displays a pattern which moves a set of colours in a single direction
    continuously.

    These colours are placed equidistant from each other and the LEDs between
    them are interpolated.
    """

    def __init__(
      self,
      leds,
      leds_per_second,
      interpolation_mode,
      colour_palette,
      display_time):
        """Creates a StreamPattern object.

        :param leds_per_second: the amount, in LED pixels, by which to move
        the position of the colours every second
        :param interpolation_mode: the InterpolationMode to use to
        interpolate between two colours on the LED strip.
        :param colour_palette: the set of colours which should be used to
        animate the pattern.
        :param display_time: the amount of time for which to display the
        pattern.
        """
        super(StreamPattern, self).__init__(display_time)
        self.leds_per_second = leds_per_second
        self.colour_palette = colour_palette
        self.interpolation_mode = interpolation_mode
        self.segment_length = (
          float(leds.get_num_leds()) / len(self.colour_palette))
        self.colour_positions = [i * self.segment_length for i in
                                 range(0, len(colour_palette))]

    def update(self, leds, delta):
        super(StreamPattern, self).update(leds, delta)
        led_offset = delta * self.leds_per_second
        self.colour_positions = [
            (led_offset + self.colour_positions[i]) % leds.get_num_leds() for i
            in range(0, len(self.colour_positions))]

        for i in range(0, len(self.colour_palette)):
            colour_index = self.colour_positions[i]
            for j in range(0, int(self.segment_length)):
                intermediate_led_index = int(math.ceil(
                  (colour_index + j)) % leds.get_num_leds())
                distance = intermediate_led_index - colour_index
                if distance < 0:
                    distance = leds.get_num_leds() + distance
                interpolated_colour = self.interpolation_mode.interpolate(
                  self.colour_palette[i],
                  self.colour_palette[(i + 1) % len(self.colour_palette)],
                  1 - (distance / self.segment_length))
                leds.set_colour(interpolated_colour, intermediate_led_index)
        leds.display()
