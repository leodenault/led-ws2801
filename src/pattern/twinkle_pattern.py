import math
import random
from colour import led_colour
from timed_pattern import TimedPattern


_AMPLITUDE = 0.5
_PHASE_SHIFT = -math.pi / 2

class _TwinklingLed:
  def __init__(self, index, twinkle_length):
    self.index = index
    self.twinkle_length = twinkle_length
    self.elapsed_time = twinkle_length
    self.angular_momentum = (2 * math.pi) / twinkle_length

  def reset(self):
    self.elapsed_time = 0

  def is_expired(self):
    return self.elapsed_time >= self.twinkle_length

  def update(self, leds, delta):
    self.elapsed_time += delta
    if self.elapsed_time < self.twinkle_length:
      brightness = self._compute_brightness()
      leds.set_colour(led_colour.OFF_WHITE.multiply(brightness), self.index)

  def _compute_brightness(self):
    return _AMPLITUDE * (math.sin(
      (self.angular_momentum * self.elapsed_time) + _PHASE_SHIFT) + 1)


class TwinklePattern(TimedPattern):
  """Twinkles lights randomly across the LED device.
  """

  def __init__(
      self,
      num_leds,
      average_time_between_twinkles,
      twinkle_length,
      display_time):
    """Creates a TwinklePattern object.

    :param num_leds: the number of LEDs on the device.
    :param average_time_between_twinkles: the average amount of time, in
    seconds, which should pass after an LED started twinkling before another
    should start twinkling.
    :param twinkle_length: the amount of time, in seconds, it takes for an
    individual LED to twinkle.
    :param display_time: the amount of time for which to display the
    pattern.
    """
    super(TwinklePattern, self).__init__(display_time)
    self.num_leds = num_leds
    self.twinkle_probability = 1.0 / average_time_between_twinkles
    self.twinkle_length = twinkle_length
    self.twinkling_leds = []
    self.available_leds = [_TwinklingLed(i, twinkle_length) for i in
                           range(num_leds)]

  def update(self, leds, delta):
    super(TwinklePattern, self).update(leds, delta)

    num_available_leds = len(self.available_leds)
    if (random.random() < self.twinkle_probability * delta
        and num_available_leds > 0):
      led_to_twinkle = self.available_leds.pop(
        random.randint(0, num_available_leds - 1))
      led_to_twinkle.reset()
      self.twinkling_leds.append(led_to_twinkle)

    leds_to_remove = []
    for i, led in enumerate(self.twinkling_leds):
      led.update(leds, delta)
      if led.is_expired():
        leds_to_remove.append(i)

    for led in leds_to_remove:
      self.available_leds.append(self.twinkling_leds.pop(led))
