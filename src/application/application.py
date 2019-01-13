import time
import random


class Application:
    """An application that drives an LED strip. This is the top-level object
    for interacting with a strip.
    """

    def __init__(self, leds, pattern_factories, pattern_display_time):
        """Creates an Application instance.

        :param leds: the LedStrip object used to interact with the LEDs.
        :param pattern_factories: A list of lambdas which instantiate a given
        pattern.
        :param pattern_display_time: the time, in seconds, that a given pattern
        should be run.
        """
        self.leds = leds
        self.pattern_factories = pattern_factories
        self.pattern_display_time = pattern_display_time

    def run(self):
        """Starts running the application.
        """
        while self.leds.is_active():
            next_factory_index = random.randint(
              0, len(self.pattern_factories) - 1)
            self._animate_pattern(self.pattern_factories[next_factory_index]())

    def _animate_pattern(self, pattern):
        print("Starting {0}!".format(pattern.__class__.__name__))
        self.leds.clear()
        start_time = time.time()
        current_time = start_time
        previous_time = 0
        while (
          self.leds.is_active()
          and current_time - start_time < self.pattern_display_time):
            delta = current_time - previous_time
            previous_time = current_time
            pattern.update(self.leds, delta)
            current_time = time.time()
