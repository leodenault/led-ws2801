from pattern.timed_pattern import TimedPattern
import math

_AMPLITUDE = 0.5
_PHASE_SHIFT = -math.pi / 2


class PulsingPattern(TimedPattern):
    """A pattern that pulses all LEDs with a given colour.

    The pattern will cycle through the colour palette given to it.
    """

    def __init__(self, colour_palette, pulse_period, display_time):
        super(PulsingPattern, self).__init__(display_time)
        self.colour_palette = colour_palette
        self.pulse_period = pulse_period
        self.angular_momentum = (2 * math.pi) / self.pulse_period

    def update(self, leds, delta):
        super(PulsingPattern, self).update(leds, delta)
        current_colour = self.colour_palette[
            int(self.elapsed_time / self.pulse_period) % len(
              self.colour_palette)]
        brightness = self._compute_brightness()
        leds.set_colour(current_colour.multiply(brightness))

    def _compute_brightness(self):
        return _AMPLITUDE * (math.sin(
          (self.angular_momentum * self.elapsed_time) + _PHASE_SHIFT) + 1)
