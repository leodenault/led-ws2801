"""Animates random patterns on a WS2801 LED strip with traditional holiday
colours.
"""

import sys

from application import application_factory
from colour import led_colour
from colour.cubic_interpolation import CubicInterpolation
from display.brightness.always_max_brightness_schedule import \
    AlwaysMaxBrightnessSchedule
from pattern.stream_pattern import StreamPattern

NUM_LEDS = 86

application_factory.create_application(
  sys.argv,
  NUM_LEDS,
  AlwaysMaxBrightnessSchedule(1.0),
  [lambda:
   StreamPattern(
     NUM_LEDS,
     10,
     CubicInterpolation(),
     [led_colour.WHITE, led_colour.RED, led_colour.GOLD, led_colour.GREEN],
     sys.maxint),
   ]).run()
