from abc import ABCMeta, abstractmethod


class BrightnessSchedule:
    """Specifies a schedule for brightening and dimming the LEDs on a strip
    connected to a Raspberry Pi.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_brightness(self):
        """Returns the brightness at which an LED should display its colour
        as a float between 0.0 and 1.0.
        """
        pass
