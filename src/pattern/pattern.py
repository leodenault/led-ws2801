from abc import ABCMeta, abstractmethod


class Pattern:
    """A pattern displayed on an LED strip.

    Implementations of this ABC will be given control of the LED lights and
    are expected to display visually appealing patterns for a limited time.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def animate(self, leds, colours):
        """Animates a particular pattern on a strip of LEDs.
        :param leds: an LedStrip reference for sending commands to the
        physical LED strip.
        :param colours: the set of colours which should be used to animate
        the pattern.
        """
        print("Starting {0}!".format(self.__class__.__name__))
