"""Factory methods for instantiating LedStrip objects using an underlying
TkinterDevice as their device.

Make sure to install Tkinter to make sure your program will function correctly.
"""

from display.led_strip import LedDirection, LedStrip
from display.tkinter.tkinter_device import TkinterDevice


def create_tkinter_led_strip(
  num_leds,
  brightness_schedule,
  direction=LedDirection.START_TO_END,
  led_width=20,
  led_height=20):
    """Creates an LedStrip instance using the TkinterDevice as
    its device.

    :param num_leds: the number of LEDs on the strip.
    :param brightness_schedule: the BrightnessSchedule object configuring
    how bright the LEDs should be depending on the time of day.
    :param direction: the direction in which animations should be
    rendered. Use LedDirection.START_TO_END to output patterns so that
    the first pixel in the pattern matches with the first physical LED on
    the strip. Use LedDirection.END_TO_START to output patterns so that
    the first pixel in the pattern matches the last physical LED on the
    strip.
    :param led_width: the width, in pixels, of each of the LEDs displayed in
    the window. Defaults to 20 pixels.
    :param led_height: the height, in pixels, of each of the LEDs displayed
    in the window. Defaults to 20 pixels.
    :return: an LedStrip object for interacting with the physical strip.
    """
    return LedStrip(
      TkinterDevice(num_leds, led_width, led_height),
      brightness_schedule, direction)
