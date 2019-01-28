import math

from renderable.spotlight import Spotlight
from timed_pattern import TimedPattern

_PHASE_SHIFT = -math.pi / 2


class SwingingSpotlightPattern(TimedPattern):
    """A pattern where two spotlights "swing" from each end of the LED strip
    to the other in inverse motion.
    """

    def __init__(
      self, colour1, colour2, spotlight_radius, swing_period, display_time):
        """Instantiates a SwingingSpotlightPattern.

        :param colour1: the colour used when rendering the first spotlight.
        :param colour2: the colour used when rendering the second spotlight.
        :param spotlight_radius: the radius of each of the spotlights.
        :param swing_period: the amount of time it takes for a full swing to
        occur.
        :param display_time: the amount of time this pattern should be
        displayed.
        """
        super(SwingingSpotlightPattern, self).__init__(display_time)
        self.elapsed_time = 0
        self.spotlight_radius = spotlight_radius
        self.spotlight1 = Spotlight(0, colour1, spotlight_radius)
        self.spotlight2 = Spotlight(0, colour2, spotlight_radius)
        self.swing_period = swing_period
        self.angular_momentum = 2 * math.pi / self.swing_period

    def update(self, leds, delta):
        super(SwingingSpotlightPattern, self).update(leds, delta)
        leds.clear()
        num_leds = leds.get_num_leds()
        self.elapsed_time += delta

        spotlight1_position = self._compute_position(num_leds)
        self.spotlight1.setPosition(spotlight1_position)
        self.spotlight2.setPosition(num_leds - spotlight1_position - 1)

        self.spotlight1.render(leds)
        self.spotlight2.render(leds)

    def _compute_position(self, num_leds):
        amplitude = (num_leds / 2.0) - self.spotlight_radius
        vertical_shift = num_leds / 2.0
        return (amplitude * math.sin(
          self.angular_momentum * self.elapsed_time + _PHASE_SHIFT) +
                vertical_shift)
