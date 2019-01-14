from abc import ABCMeta, abstractmethod


class Pattern:
    """A pattern displayed on an LED strip.

    Implementations of this ABC are expected to display visually appealing
    patterns for a limited time.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, leds, delta):
        """Updates the pattern.

        :param leds: an LedStrip reference for sending commands to the
        physical LED strip.
        :param delta: the amount of time that has passed since the last update.
        """
        pass

    @abstractmethod
    def is_done(self):
        """
        :return: whether this pattern has finished animating or not.
        """
        pass
