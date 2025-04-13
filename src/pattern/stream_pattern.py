import math

from pattern.timed_pattern import TimedPattern


def create_colour_cycle(
    base_colours, total_colours, inidividual_colour_length=1):
  """Creates a list of colours which cycles through the base set of colours.

  :param base_colours: the base set of colours which will be repeated in
  the returned list of colours.
  :param total_colours: the total number of colours which should appear in
  the returned list of colours.
  :param inidividual_colour_length: the number of LEDs used by an individual
  colour.
  :return: a list of colours containing the set of colours in base_colours
  repeated cyclically.
  """
  return [
    base_colours[
      i / inidividual_colour_length % len(base_colours)
      ] for i in range(0, total_colours)]


class StreamPattern(TimedPattern):
  """Displays a pattern which moves a set of colours in a single direction
  continuously.

  These colours are placed equidistant from each other and the LEDs between
  them are interpolated.
  """

  def __init__(
      self,
      num_leds,
      period,
      interpolation_mode,
      colour_palette,
      display_time):
    """Creates a StreamPattern object.

    :param num_leds: the number of LEDs on the device.
    :param period: the amount of time for a colour to wrap around the LED
    strip.
    :param interpolation_mode: the InterpolationMode to use to
    interpolate between two colours on the LED strip.
    :param colour_palette: the set of colours which should be used to
    animate the pattern.
    :param display_time: the amount of time for which to display the
    pattern.
    """
    super(StreamPattern, self).__init__(display_time)
    self.period = period
    self.colour_palette = colour_palette
    self.interpolation_mode = interpolation_mode
    self.segment_length = (
        float(num_leds) / len(self.colour_palette))

  def update(self, leds, delta):
    super(StreamPattern, self).update(leds, delta)
    num_leds = leds.get_num_leds()
    led_offset = (
        ((self.elapsed_time % self.period) / self.period) * num_leds)
    num_colours = len(self.colour_palette)

    for i in range(0, num_colours):
      colour_position = (i * self.segment_length + led_offset) % num_leds
      j = 0
      while math.ceil(
          colour_position + j) < colour_position + self.segment_length:
        intermediate_led_index = int(math.ceil(
          (colour_position + j)) % num_leds)
        distance = intermediate_led_index - colour_position
        if distance < 0:
          distance += num_leds
        interpolated_colour = self.interpolation_mode.interpolate(
          self.colour_palette[i],
          self.colour_palette[(i + 1) % num_colours],
          1 - (distance / self.segment_length))
        leds.set_colour(interpolated_colour, intermediate_led_index)
        j += 1
