from Tkinter import Frame

from led_widget import LedWidget


class LedStripWidget:
    """Tk widget displaying an LED strip.
    """

    def __init__(self, master, num_leds, led_width, led_height):
        """Instantiates an LED strip widget.

        :param master: the parent container of this widget.
        :param num_leds: the number of LEDs to display.
        :param led_width: the width of each of the LEDs.
        :param led_height: the height of each of the LEDs.
        """
        self.led_container = Frame(master)
        self.leds = self._create_leds(num_leds, led_width, led_height)

    def _create_leds(self, num_leds, led_width, led_height):
        leds = []
        for i in range(0, num_leds):
            leds.append(LedWidget(self.led_container, led_width, led_height))
        return leds

    def pack(self, options):
        """Displays and arranges, geometrically, this widget.

        :param options: the Tk options to use when packing this widget.
        """
        self.led_container.pack(options)
        for i in range(0, len(self.leds)):
            self.leds[i].pack({"side": "left"})

    def set_colour_at(self, index, colour):
        """Sets the colour of an LED at the given index.

        :param index: the index of the LED whose colour must be set.
        :param colour: the colour that the LED will be set to.
        """
        self.leds[index].set_led_colour(colour)
