from abc import ABCMeta
from abc import abstractmethod


class LedDirection:
    """Enum class for defining directions to output light patterns on an LED
    strip connected to a Raspberry Pi.
    """

    START_TO_END = 0
    """Output patterns so that 
        the first pixel in the pattern matches with the first physical LED on 
        the strip.
    """
    END_TO_START = 1
    """Output patterns so that 
        the first pixel in the pattern matches with the last physical LED on 
        the strip
    """


class Display:
    """Abstraction around a WS2801 LED strip connected to a Raspberry Pi
    through its GPIO pins and communicating through SPI.
    """

    __metaclass__ = ABCMeta

    _ALL_LEDS = -1

    @abstractmethod
    def set_colour(self, colour, led=_ALL_LEDS):
        """Sets the colour of one or all LEDs on a strip.

        :param colour: the colour to output to the LED.
        :param led: the index of the LED to output the colour to. If
        unspecified, then colour is displayed on all LEDs.
        """
        pass

    @abstractmethod
    def set_colour_and_display(self, colour, led=_ALL_LEDS):
        """Sets the colour of one or all LEDs on a strip and then displays it.

        :param colour: the colour to output to the LED.
        :param led: the index of the LED to output the colour to. If
        unspecified, then colour is displayed on all LEDs.
        """
        pass

    @abstractmethod
    def display(self):
        """Displays the colours currently assigned to the LEDs.
        """
        pass

    @abstractmethod
    def clear(self):
        """Clears the LED strip of any colours currently displayed.
        """
        pass

    @abstractmethod
    def get_colour_at(self, index):
        """Returns the colour at the provided logical index.
        """
        pass
