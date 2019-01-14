"""Animates random patterns on a WS2801 LED strip with traditional holiday
colours.
"""

from application.application import Application
from colour import led_colour, palette
from colour.cubic_interpolation import CubicInterpolation
from colour.linear_interpolation import LinearInterpolation
from colour.no_interpolation import NoInterpolation
from colour.quadratic_interpolation import QuadraticInterpolation
from display.brightness.always_max_brightness_schedule import \
    AlwaysMaxBrightnessSchedule
from display.tkinter import tkinter_led_strip_factory
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
      leds.get_num_leds())


leds = tkinter_led_strip_factory.create_tkinter_led_strip(
  86,
  AlwaysMaxBrightnessSchedule(1.0))

patterns = [
    # Multi-colour stream pattern.
    lambda:
    StreamPattern(
      leds,
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
        leds.get_num_leds()),
      10),
    # Binary colour stream pattern.
    lambda:
    StreamPattern(
      leds,
      4,
      NoInterpolation(),
      stream_pattern.create_colour_cycle(
        palette.choose_random_from(
          [led_colour.WHITE, led_colour.RED, led_colour.GREEN,
           led_colour.GOLD],
          2,
          2),
        leds.get_num_leds()),
      10),
    # Smooth stream pattern.
    lambda:
    StreamPattern(
      leds,
      10,
      CubicInterpolation(),
      [led_colour.WHITE, led_colour.RED, led_colour.GOLD, led_colour.GREEN],
      10),
    # Phasing stream pattern.
    lambda:
    StreamPattern(
      leds,
      0.25,
      LinearInterpolation(),
      stream_pattern.create_colour_cycle(
        [led_colour.RED, led_colour.GREEN, led_colour.BLUE],
        leds.get_num_leds()),
      10),
    # Sort patterns.
    lambda:
    sort_patterns.create_bubble_sort_pattern(
      leds,
      5,
      0.02,
      5,
      1.5,
      _generate_sort_palette()),
    lambda:
    sort_patterns.create_merge_sort_pattern(
      leds,
      0.5,
      0.08,
      5,
      1.5,
      _generate_sort_palette()),
    # Snow pattern.
    lambda: SnowPattern(led_colour.WHITE, 0.1, 0.2, 10),
]

app = Application(leds, patterns)
app.run()
