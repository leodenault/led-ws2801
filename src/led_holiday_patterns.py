"""Animates random patterns on a WS2801 LED strip with traditional holiday
colours.
"""

import random

from colour import led_colour
from colour import palette
from colour.cubic_interpolation import CubicInterpolation
from colour.linear_interpolation import LinearInterpolation
from colour.no_interpolation import NoInterpolation
from colour.quadratic_interpolation import QuadraticInterpolation
from display.led_strip import LedDirection
from display.led_strip import LedStrip
from display.brightness.regular_brightness_schedule import \
    RegularBrightnessSchedule
from display.adafruit_ws2801.adafruit_ws2801_led_strip_controller_adapter \
    import \
    AdafruitWs2801LedStripControllerAdapter
from pattern import stream_pattern
from pattern.snow_pattern import SnowPattern
from pattern.sorting.bubble_sort_pattern import BubbleSortPattern
from pattern.sorting.colour_distributor import ColourDistributor
from pattern.sorting.merge_sort_pattern import MergeSortPattern
from pattern.sorting.sort_celebration import SortCelebration
from pattern.stream_pattern import StreamPattern


def _generate_sort_palette(sort_pattern):
    candidates = palette.choose_random_from(
      [led_colour.WHITE, led_colour.GREEN, led_colour.RED, led_colour.BLACK],
      2,
      2)
    return sort_pattern.animate(
      leds,
      palette.gradient(
        candidates[0],
        candidates[1],
        QuadraticInterpolation(),
        leds.get_num_leds()))


leds = LedStrip(
  AdafruitWs2801LedStripControllerAdapter(86),
  RegularBrightnessSchedule(7, 9, 16, 21, 0.1, 1.0),
  LedDirection.END_TO_START)

colour_distributor = ColourDistributor(5)
sort_celebration = SortCelebration(5, 1.5)

snow_pattern = SnowPattern(30, 0.1, 0.2)
bubble_sort_pattern = BubbleSortPattern(
  colour_distributor,
  sort_celebration,
  0.02)
merge_sort_pattern = MergeSortPattern(
  colour_distributor,
  sort_celebration,
  0.08)
multi_colour_stream_pattern = StreamPattern(30, 6, NoInterpolation())
binary_colour_stream_pattern = StreamPattern(30, 4, NoInterpolation())
smooth_stream_pattern = StreamPattern(30, 10, CubicInterpolation())
phasing_stream_pattern = StreamPattern(30, 0.25, LinearInterpolation())

patterns = [
    # Multi-colour stream pattern.
    lambda:
    multi_colour_stream_pattern.animate(
      leds,
      stream_pattern.create_colour_cycle(
        palette.choose_random_from([
            led_colour.WHITE,
            led_colour.RED,
            led_colour.GREEN,
            led_colour.BLUE,
            led_colour.GOLD],
          4,
          5),
        leds.get_num_leds())),
    # Binary colour stream pattern.
    lambda: binary_colour_stream_pattern.animate(
      leds,
      stream_pattern.create_colour_cycle(
        palette.choose_random_from(
          [led_colour.WHITE, led_colour.RED, led_colour.GREEN, led_colour.GOLD],
          2,
          2),
        leds.get_num_leds())),
    # Smooth stream pattern.
    lambda:
    smooth_stream_pattern.animate(
      leds,
      [led_colour.WHITE, led_colour.RED, led_colour.GOLD, led_colour.GREEN]),
    # Phasing stream pattern.
    lambda:
    phasing_stream_pattern.animate(
      leds,
      stream_pattern.create_colour_cycle(
        [led_colour.RED, led_colour.GREEN, led_colour.BLUE],
        leds.get_num_leds())),
    # Sort patterns.
    lambda: _generate_sort_palette(merge_sort_pattern),
    lambda: _generate_sort_palette(bubble_sort_pattern),
    # Snow pattern.
    lambda: snow_pattern.animate(leds, [led_colour.WHITE]),
]

leds.clear()

while True:
    patterns[random.randint(0, len(patterns) - 1)]()
