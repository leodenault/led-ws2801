"""Animates random patterns on a WS2801 LED strip with traditional holiday
colours.
"""

import sys

from application import application_factory
from colour import led_colour, palette
from colour.cubic_interpolation import CubicInterpolation
from colour.led_colour import Colour
from display.brightness.always_max_brightness_schedule import \
    AlwaysMaxBrightnessSchedule
from pattern.stream_pattern import StreamPattern

NUM_LEDS = 71

application_factory.create_application(
  sys.argv,
  NUM_LEDS,
  AlwaysMaxBrightnessSchedule(1.0),
  [lambda:
   StreamPattern(
     NUM_LEDS,
     10,
     CubicInterpolation(),
     palette.choose_random_from(
       [
           led_colour.RED,
           led_colour.GOLD,
           led_colour.PURPLE,
           led_colour.CYAN,
           Colour(0, 64, 128)]),
     30),
   ]).run()
