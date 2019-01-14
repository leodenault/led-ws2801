import random
import time

from colour import led_colour
from timed_pattern import TimedPattern


class SnowPattern(TimedPattern):
    """Animates small white lights on an LED strip as if they were snow
    moving from one end of the strip to the other.
    """

    def __init__(self, colour, spawn_rate, movement_period, display_time):
        """Creates a SnowPattern object for animating an LED strip.

        :param colour: the colour used to display the snowflakes.
        :param duration: the amount of time the pattern should be displayed.
        :param spawn_rate: the rate at which the snowflakes should spawn
        :param movement_period: the amount of time it takes for a snowflake
        to move from one LED to another.
        expressed as a float between 0.0 and 1.0.
        :param display_time: the amount of time for which to display the
        pattern.
        """
        super(SnowPattern, self).__init__(display_time)
        self.colour = colour
        self.spawn_rate = spawn_rate
        self.movement_period = movement_period
        self.snowflakes = []

    def update(self, leds, delta):
        super(SnowPattern, self).update(leds, delta)
        num_snowflakes = len(self.snowflakes)
        for i in range(0, num_snowflakes):
            snowflake_pixel = self.snowflakes[i]
            leds.set_colour(led_colour.BLACK, snowflake_pixel)
            self.snowflakes[i] += 1

        if (num_snowflakes > 0
          and self.snowflakes[num_snowflakes - 1] >= leds.get_num_leds()):
            self.snowflakes.pop(num_snowflakes - 1)
            num_snowflakes -= 1

        new_snowflake = (
          0 not in self.snowflakes
          and 1 not in self.snowflakes
          and random.random() > 1 - self.spawn_rate)
        if new_snowflake:
            self.snowflakes.insert(0, 0)
            num_snowflakes += 1

        for i in range(0, num_snowflakes):
            snowflake_pixel = self.snowflakes[i]
            leds.set_colour(self.colour, snowflake_pixel)
        leds.display()
        time.sleep(self.movement_period)
