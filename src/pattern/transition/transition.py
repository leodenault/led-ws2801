from abc import ABCMeta
from abc import abstractmethod
from pattern.pattern import Pattern


class Transition(Pattern):
    """Handles transitioning from one pattern to the next.
    """

    __metaclass__ = ABCMeta

    def __init__(self, pattern1, pattern2):
        """Creates a Transition instance.

        :param pattern1: the pattern from which we are transitioning.
        :param pattern2: the pattern to which we are transitioning.
        """
        self.pattern1 = pattern1
        self.pattern2 = pattern2

    def update(self, leds, delta):
        self.update_before_first_pattern(leds, delta)
        self.pattern1.update(leds, delta)
        self.update_before_second_pattern(leds, delta)
        self.pattern2.update(leds, delta)
        self.update_after_second_pattern(leds, delta)

    @abstractmethod
    def update_before_first_pattern(self, leds, delta):
        """Updates the transition state before rendering the pattern from
        which we are transitioning.

        :param leds: an LedStrip reference for sending commands to the
        physical LED strip.
        :param delta: the amount of time that has passed since the last update.
        """
        pass

    @abstractmethod
    def update_before_second_pattern(self, leds, delta):
        """Updates the transition state after rendering the pattern from
        which we are transitioning but before the pattern to which we are
        transitioning.

        :param leds: an LedStrip reference for sending commands to the
        physical LED strip.
        :param delta: the amount of time that has passed since the last update.
        """
        pass

    @abstractmethod
    def update_after_second_pattern(self, leds, delta):
        """Updates the transition state after rendering the pattern to which
        we are transitioning.

        :param leds: an LedStrip reference for sending commands to the
        physical LED strip.
        :param delta: the amount of time that has passed since the last update.
        """
        pass
