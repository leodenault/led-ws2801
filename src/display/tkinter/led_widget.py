from Tkinter import Frame
from colour.led_colour import Colour
from colour import led_colour

class LedWidget:
    """Tk widget representing an LED on a strip.
    """

    def __init__(self, master, width, height):
        """Instantiates an LED widget.

        :param master: the parent container of this widget.
        :param width: the width of this widget.
        :param height: the height of thie widget.
        """
        self.widget = Frame(master)
        self.widget["bg"] = "black"
        self.colour = led_colour.BLACK
        self.widget["highlightbackground"] = "grey"
        self.widget["highlightthickness"] = 1
        self.widget["width"] = width
        self.widget["height"] = height

    def pack(self, options):
        """Displays and arranges, geometrically, this widget.

        :param options: the Tk options to use when packing this widget.
        """
        self.widget.pack(options)

    def set_led_colour(self, colour):
        """Sets the colour of the LED widget to the given colour.
        """
        self.widget["bg"] = _convert_colour_to_hex(colour)
        self.colour = colour.copy()

    def get_led_colour(self):
        """Returns the colour of the LED widget.
        """
        return self.colour


def _convert_colour_to_hex(colour):
    return ("#" + _component_to_hex(colour.r) + _component_to_hex(colour.g)
            + _component_to_hex(colour.b))


def _component_to_hex(component):
    return (
        hex(component)[2:] if component >= 16 else "0" + hex(component)[2:])
