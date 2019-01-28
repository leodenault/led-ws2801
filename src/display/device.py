from abc import ABCMeta
from abc import abstractmethod


class Device:
    """LED strip device which has the ability to display RGB colours on a
    series of LEDs.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def set_led_colour(self, index, colour):
        """Sets the colour for the LED at a specific index.

        :param index: the index of the LED on the device.
        :param colour: the colour that should be displayed on the LED.
        """
        pass

    @abstractmethod
    def get_led_colour(self, index):
        """Gets the colour for the LED at the specific index.

        :param index: the index of the LED whose colour should be returned
        """
        pass

    @abstractmethod
    def show(self):
        """Signals to the device that it should display whatever colours have
        been set on it.
        """

    @abstractmethod
    def clear(self):
        """Clears all of the LEDs controlled by this device.
        """

    @abstractmethod
    def get_num_leds(self):
        """
        :return: the number of LEDs on this device.
        """

    @abstractmethod
    def is_active(self):
        """
        :return: Whether the device is currently active or has shut down.
        """
        pass
