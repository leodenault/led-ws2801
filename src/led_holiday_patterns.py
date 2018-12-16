"""Animates random patterns on a WS2801 LED strip with traditional holiday
colours.
"""

import random

from colour import led_colour
from colour.cubic_interpolation import CubicInterpolation
from colour.no_interpolation import NoInterpolation
from led_strip.led_strip import LedDirection
from led_strip.led_strip import LedStrip
from led_strip.regular_brightness_schedule import RegularBrightnessSchedule
from pattern import stream_pattern
from pattern.snow_pattern import SnowPattern
from pattern.sorting.bubble_sort_pattern import BubbleSortPattern
from pattern.sorting.colour_distributor import ColourDistributor
from pattern.sorting.merge_sort_pattern import MergeSortPattern
from pattern.sorting.sort_celebration import SortCelebration
from pattern.stream_pattern import StreamPattern

leds = LedStrip(
  86,
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

patterns = [
    # Multi-colour stream patterns.
    lambda:
    multi_colour_stream_pattern.animate(
      leds,
      stream_pattern.create_colour_cycle([
          led_colour.WHITE,
          led_colour.RED,
          led_colour.GREEN,
          led_colour.GOLD],
        leds.num_leds)),
    lambda:
    multi_colour_stream_pattern.animate(
      leds,
      stream_pattern.create_colour_cycle([
          led_colour.WHITE,
          led_colour.RED,
          led_colour.GREEN,
          led_colour.BLUE],
        leds.num_leds)),
    lambda:
    multi_colour_stream_pattern.animate(
      leds,
      stream_pattern.create_colour_cycle([
          led_colour.WHITE,
          led_colour.RED,
          led_colour.GREEN,
          led_colour.BLUE,
          led_colour.GOLD],
        leds.num_leds)),
    # Binary colour stream patterns.
    lambda: binary_colour_stream_pattern.animate(
      leds,
      stream_pattern.create_colour_cycle(
        [led_colour.WHITE, led_colour.RED],
        leds.num_leds)),
    lambda: binary_colour_stream_pattern.animate(
      leds,
      stream_pattern.create_colour_cycle(
        [led_colour.GREEN, led_colour.RED],
        leds.num_leds)),
    lambda: binary_colour_stream_pattern.animate(
      leds,
      stream_pattern.create_colour_cycle(
        [led_colour.GOLD, led_colour.RED],
        leds.num_leds)),
    lambda: binary_colour_stream_pattern.animate(
      leds,
      stream_pattern.create_colour_cycle(
        [led_colour.GREEN, led_colour.WHITE],
        leds.num_leds)),
    # Smooth stream patterns.
    lambda:
    smooth_stream_pattern.animate(
      leds,
      [led_colour.WHITE, led_colour.RED, led_colour.GOLD, led_colour.GREEN]),
    # Sort patterns.
    lambda: merge_sort_pattern.animate(
      leds,
      [led_colour.WHITE, led_colour.RED, led_colour.GREEN, led_colour.GOLD]),
    lambda: bubble_sort_pattern.animate(
      leds,
      [led_colour.WHITE, led_colour.RED, led_colour.GREEN, led_colour.GOLD]),
    lambda: snow_pattern.animate(leds, [led_colour.WHITE]),
]

leds.clear()

while True:
    patterns[random.randint(0, len(patterns) - 1)]()
