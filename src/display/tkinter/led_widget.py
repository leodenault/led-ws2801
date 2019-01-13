from Tkinter import Frame


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
        self.widget["bg"] = self._convert_colour_to_hex(colour)

    def _convert_colour_to_hex(self, colour):
        return "#" + str(hex(colour.r)) + str(hex(colour.g)) + str(
          hex(colour.b))
