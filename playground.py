"""Playground library for experimenting with WS2801 LEDs.

This module is meant to be imported when experimenting on the python CLI with
an LED strip.
"""

import Adafruit_GPIO.SPI as SPI
import Adafruit_WS2801

_ALL_LEDS = -1


class Playground:
    def __init__(self, pixel_count, start_to_end, spi_port=0, spi_device=0):
        """Creates a playground object for experimenting with WS2801 LEDs.

        :param pixel_count: the number of pixels to output to. This is
        usually the total number of LEDs on the strip.
        :param start_to_end: True if index 0 should correspond to the first
        LED on the strip, False if it should correspond to the last LED on
        the strip (with index 1 corresponding to the next-to-last LED,
        and so on).
        :param spi_port: the SPI port to output to. Defaults to 0.
        :param spi_device: the SPI device to output to. For example, a value
        of 0 would output to /dev/spidev0.0, a value of 1 outputs to
        /dev/spidev0.1. Defaults to 0.
        """

        self.pixel_count = pixel_count
        self.start_to_end = start_to_end
        self.pixels = Adafruit_WS2801.WS2801Pixels(
          pixel_count, spi=SPI.SpiDev(spi_port, spi_device))

    def display(self, colour, led=_ALL_LEDS):
        """Displays a specific colour on a specific LED.

        :param colour: the colour to output to the LED.
        :param led: the index of the LED to output the colour to. If
        unspecified, then colour is displayed on all LEDs.
        """

        if led == _ALL_LEDS:
            for i in range(0, self.pixel_count):
                self.pixels.set_pixel_rgb(i, colour.r, colour.g, colour.b)
        else:
            led = led if self.start_to_end else self.pixel_count - led - 1
            self.pixels.set_pixel_rgb(led, colour.r, colour.g, colour.b)
        self.pixels.show()

    def clear(self):
        """Clears the LED strip of any colours currently displayed.
        """

        self.pixels.clear()
        self.pixels.show()
