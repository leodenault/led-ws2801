import random
import time

from pattern.transition.fading_transition import FadingTransition


class Application:
    """An application that drives an LED strip. This is the top-level object
    for interacting with a strip.
    """

    def __init__(self, leds, transition_length, pattern_factories):
        """Creates an Application instance.

        :param leds: the LedStrip object used to interact with the LEDs.
        :param transition_length: the length of time, in seconds,
        for a transition to execute.
        :param pattern_factories: A list of lambdas which instantiate a given
        pattern.
        """
        self.leds = leds
        self.transition_length = transition_length
        self.pattern_factories = pattern_factories
        self.current_pattern = self._get_random_pattern()
        self.elapsed_time = 0

    def run(self):
        """Starts running the application.
        """
        while self.leds.is_active():
            self._animate_pattern(self.current_pattern)
            next_pattern = self._get_random_pattern()
            self._animate_pattern(
              FadingTransition(
                self.current_pattern, next_pattern, self.transition_length))
            self.current_pattern = next_pattern

    def _animate_pattern(self, pattern):
        print("Starting {0}!".format(pattern.__class__.__name__))
        current_time = time.time()
        previous_time = current_time
        while self.leds.is_active() and not pattern.is_done():
            delta = current_time - previous_time
            previous_time = current_time
            self.elapsed_time += delta
            self.leds.clear()
            pattern.update(self.leds, delta)
            self.leds.display()
            current_time = time.time()

    def _get_random_pattern(self):
        return self.pattern_factories[
            random.randint(0, len(self.pattern_factories) - 1)]()
