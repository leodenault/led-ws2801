"""Animates random patterns on a WS2801 LED strip with traditional holiday
colours.
"""

import sys

from application.application import Application
from colour import led_colour
from colour.cubic_interpolation import CubicInterpolation
from display.adafruit_ws2801 import adafruit_led_strip_factory
from display.brightness.always_max_brightness_schedule import \
    AlwaysMaxBrightnessSchedule
from pattern.stream_pattern import StreamPattern

leds = adafruit_led_strip_factory.create_adafruit_led_strip(
  86,
  AlwaysMaxBrightnessSchedule(1.0))

patterns = [
    # Smooth stream pattern.
    lambda:
    StreamPattern(
      leds,
      10,
      CubicInterpolation(),
      [led_colour.WHITE, led_colour.RED, led_colour.GOLD, led_colour.GREEN],
      sys.maxint),
]

app = Application(leds, patterns)
app.run()
