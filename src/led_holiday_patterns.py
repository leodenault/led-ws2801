"""Animates random patterns on a WS2801 LED strip with traditional holiday
colours.
"""

import sys

from application import application_factory
from colour import led_colour, palette
from colour.cubic_interpolation import CubicInterpolation
from colour.linear_interpolation import LinearInterpolation
from colour.no_interpolation import NoInterpolation
from colour.quadratic_interpolation import QuadraticInterpolation
from display.brightness.regular_brightness_schedule import \
    RegularBrightnessSchedule
from display.led_strip import LedDirection
from pattern import stream_pattern
from pattern.snow_pattern import SnowPattern
from pattern.sorting import sort_patterns
from pattern.stream_pattern import StreamPattern


def _generate_sort_palette():
    candidates = palette.choose_random_from(
      [led_colour.WHITE, led_colour.GREEN, led_colour.RED, led_colour.BLACK],
      2,
      2)
    return palette.gradient(
      candidates[0],
      candidates[1],
      QuadraticInterpolation(),
      NUM_LEDS)


NUM_LEDS = 86
PATTERN_DISPLAY_TIME = 30

application_factory.create_application(
  sys.argv,
  NUM_LEDS,
  RegularBrightnessSchedule(7, 9, 16, 21, 0.1, 1.0),
  5,
  [
      # Multi-colour stream pattern.
      lambda:
      StreamPattern(
        NUM_LEDS,
        6,
        NoInterpolation(),
        stream_pattern.create_colour_cycle(
          palette.choose_random_from([
              led_colour.WHITE,
              led_colour.RED,
              led_colour.GREEN,
              led_colour.BLUE,
              led_colour.GOLD],
            4,
            5),
          NUM_LEDS),
        PATTERN_DISPLAY_TIME),
      # Binary colour stream pattern.
      lambda:
      StreamPattern(
        NUM_LEDS,
        4,
        NoInterpolation(),
        stream_pattern.create_colour_cycle(
          palette.choose_random_from(
            [led_colour.WHITE, led_colour.RED, led_colour.GREEN,
             led_colour.GOLD],
            2,
            2),
          NUM_LEDS),
        PATTERN_DISPLAY_TIME),
      # Smooth stream pattern.
      lambda:
      StreamPattern(
        NUM_LEDS,
        10,
        CubicInterpolation(),
        [led_colour.WHITE, led_colour.RED, led_colour.GOLD, led_colour.GREEN],
        PATTERN_DISPLAY_TIME),
      # Phasing stream pattern.
      lambda:
      StreamPattern(
        NUM_LEDS,
        0.25,
        LinearInterpolation(),
        stream_pattern.create_colour_cycle(
          [led_colour.RED, led_colour.GREEN, led_colour.BLUE],
          NUM_LEDS),
        PATTERN_DISPLAY_TIME),
      # Sort patterns.
      lambda:
      sort_patterns.create_bubble_sort_pattern(
        NUM_LEDS,
        5,
        0.02,
        5,
        1.5,
        _generate_sort_palette()),
      lambda:
      sort_patterns.create_merge_sort_pattern(
        NUM_LEDS,
        0.5,
        0.08,
        5,
        1.5,
        _generate_sort_palette()),
      # Snow pattern.
      lambda: SnowPattern(led_colour.WHITE, 0.1, 0.2, PATTERN_DISPLAY_TIME),
  ],
  LedDirection.END_TO_START).run()
