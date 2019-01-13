import random
import time

from colour import led_colour
from pattern import Pattern


class SnowPattern(Pattern):
    """Animates small white lights on an LED strip as if they were snow
    moving from one end of the strip to the other.
    """

    def __init__(self, duration, spawn_rate, movement_period):
        """Creates a SnowPattern object for animating an LED strip.

        :param duration: the amount of time the pattern should be displayed.
        :param spawn_rate: the rate at which the snowflakes should spawn
        :param movement_period: the amount of time it takes for a snowflake
        to move from one LED to another.
        expressed as a float between 0.0 and 1.0.
        """
        self.duration = duration
        self.spawn_rate = spawn_rate
        self.movement_period = movement_period

    def animate(self, leds, colour_palette):
        super(SnowPattern, self).animate(leds, colour_palette)
        start_time = time.time()
        leds.clear()
        snowflakes = []

        while time.time() - start_time < self.duration:
            num_snowflakes = len(snowflakes)
            for i in range(0, num_snowflakes):
                snowflake_pixel = snowflakes[i]
                leds.set_colour(led_colour.BLACK, snowflake_pixel)
                snowflakes[i] += 1

            if (num_snowflakes > 0
              and snowflakes[num_snowflakes - 1] >= leds.get_num_leds()):
                snowflakes.pop(num_snowflakes - 1)
                num_snowflakes -= 1

            new_snowflake = (
              0 not in snowflakes
              and 1 not in snowflakes
              and random.random() > 1 - self.spawn_rate)
            if new_snowflake:
                snowflakes.insert(0, 0)
                num_snowflakes += 1

            for i in range(0, num_snowflakes):
                snowflake_pixel = snowflakes[i]
                leds.set_colour(
                  led_colour.WHITE if len(colour_palette) == 0 else colour_palette[0],
                  snowflake_pixel)
            leds.display()
            time.sleep(self.movement_period)
