"""Animates random patterns on a WS2801 LED strp mounted on desktop furniture
for an aesthetically pleasing effect.
"""

import sys

from application import application_factory
from colour import led_colour, palette
from colour.cubic_interpolation import CubicInterpolation
from colour.led_colour import Colour
from display.brightness.always_max_brightness_schedule import \
    AlwaysMaxBrightnessSchedule
from pattern.stream_pattern import StreamPattern
from pattern.swinging_spotlight_pattern import SwingingSpotlightPattern
from pattern.pulsing_pattern import PulsingPattern

NUM_LEDS = 71

application_factory.create_application(
  sys.argv,
  NUM_LEDS,
  AlwaysMaxBrightnessSchedule(1.0),
  5,
  [
      lambda:
      PulsingPattern(
        [led_colour.RED, led_colour.BLUE, led_colour.PURPLE], 7.5, 40),
      lambda:
      SwingingSpotlightPattern(
        palette.choose_random_from([led_colour.PURPLE, led_colour.RED], 1, 1)[
            0],
        palette.choose_random_from([led_colour.PURPLE, led_colour.RED], 1, 1)[
            0],
        7,
        7.5,
        40),
      lambda:
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
