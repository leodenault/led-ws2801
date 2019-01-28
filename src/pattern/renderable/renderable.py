from abc import ABCMeta
from abc import abstractmethod


class Renderable:
    """An object that is able to update and render itself on an LED strip.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def render(self, leds):
        """Tells this renderable to draw itself on the LED strip.

        :param leds: the LedStrip object with which to interact.
        """
        pass

    @abstractmethod
    def setPosition(self, position):
        """Sets the position of this renderable on the strip.

        :param position: the position, as a float, at which to draw this
        renderable.
        """
        pass
