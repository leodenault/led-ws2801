from Tkinter import Frame, Tk

from display.device import Device
from led_strip_widget import LedStripWidget


class TkinterDevice(Device):
    """Device which instantiates a Tk window for testing LEDs on a computer.
    """
    def __init__(self, num_leds, led_width, led_height):
        """Instantiates a TkinterDevice.

        :param num_leds: the number of LEDs which should be displayed.
        :param led_width: the width, in pixels, of each of the LEDs.
        :param led_height: the height, in pixels, of each of the LEDs.
        """
        self._is_active = True

        self.tk = Tk()
        self.tk.protocol("WM_DELETE_WINDOW", self._on_closing)
        self.tk["bg"] = "black"
        self.top_widget = Frame(self.tk)
        self.top_widget.pack()

        self.led_strip = LedStripWidget(
          self.top_widget, num_leds, led_width, led_height)
        self.led_strip.pack({"side": "top"})

    def set_led_colour(self, index, colour):
        self.led_strip.set_colour_at(index, colour)

    def show(self):
        self.top_widget.update_idletasks()
        self.top_widget.update()

    def clear(self):
        self.led_strip.clear()

    def get_num_leds(self):
        return self.led_strip.get_num_leds()

    def _on_closing(self):
        self._is_active = False
        self.tk.destroy()

    def is_active(self):
        return self._is_active
