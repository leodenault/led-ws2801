import time
import random


class Application:
    """An application that drives an LED strip. This is the top-level object
    for interacting with a strip.
    """

    def __init__(self, leds, pattern_factories):
        """Creates an Application instance.

        :param leds: the LedStrip object used to interact with the LEDs.
        :param pattern_factories: A list of lambdas which instantiate a given
        pattern.
        """
        self.leds = leds
        self.pattern_factories = pattern_factories

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
        current_time = time.time()
        previous_time = current_time
        while self.leds.is_active() and not pattern.is_done():
            delta = current_time - previous_time
            previous_time = current_time
            pattern.update(self.leds, delta)
            self.leds.display()
            current_time = time.time()
