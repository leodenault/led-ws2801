"""Animates random patterns on a WS2801 LED strip mounted on desktop furniture
for an aesthetically pleasing effect.
"""

import sys

from application import application_factory
from colour import led_colour, palette
from colour.cubic_interpolation import CubicInterpolation
from colour.led_colour import Colour
from datetime import datetime
from display.brightness.always_max_brightness_schedule import \
  AlwaysMaxBrightnessSchedule
from pattern.stream_pattern import StreamPattern
from pattern.swinging_spotlight_pattern import SwingingSpotlightPattern
from pattern.pulsing_pattern import PulsingPattern
from pattern.twinkle_pattern import TwinklePattern

NUM_LEDS = 71
REGULAR_PATTERNS = [
  lambda:
  PulsingPattern(
    colour_palette=[led_colour.RED, led_colour.BLUE, led_colour.PURPLE],
    pulse_period=7.5,
    display_time=40),
  lambda:
  SwingingSpotlightPattern(
    colour1=palette.choose_random_from(
      [led_colour.PURPLE, led_colour.RED], 1, 1
    )[0],
    colour2=palette.choose_random_from(
      [led_colour.PURPLE, led_colour.RED], 1, 1
    )[0],
    spotlight_radius=7,
    swing_period=7.5,
    display_time=40),
  lambda:
  StreamPattern(
    num_leds=NUM_LEDS,
    period=10,
    interpolation_mode=CubicInterpolation(),
    colour_palette=palette.choose_random_from(
      [
        led_colour.RED,
        led_colour.GOLD,
        led_colour.PURPLE,
        led_colour.CYAN,
        Colour(0, 64, 128)]),
    display_time=30),
]
HOLIDAY_PATTERNS = [
  lambda:
  PulsingPattern(
    colour_palette=[
      led_colour.RED,
      led_colour.WHITE,
      led_colour.GOLD,
      led_colour.BLUE,
      led_colour.WHITE,
      led_colour.GREEN
    ],
    pulse_period=5,
    display_time=30
  ),
  lambda:
  StreamPattern(
    num_leds=NUM_LEDS,
    period=5,
    interpolation_mode=CubicInterpolation(),
    colour_palette=palette.choose_random_from(
      [
        led_colour.RED,
        led_colour.GOLD,
        led_colour.WHITE,
        led_colour.GREEN]),
    display_time=30
  ),
  lambda:
  StreamPattern(
    num_leds=NUM_LEDS,
    period=10,
    interpolation_mode=CubicInterpolation(),
    colour_palette=palette.choose_random_from(
      [
        led_colour.BLUE,
        led_colour.GOLD,
        led_colour.WHITE]),
    display_time=30
  ),
  lambda:
  TwinklePattern(
    num_leds=NUM_LEDS,
    average_time_between_twinkles=0.5,
    twinkle_length=5,
    display_time=30
  ),
  lambda:
  TwinklePattern(
    num_leds=NUM_LEDS,
    average_time_between_twinkles=0.3,
    twinkle_length=1,
    display_time=30
  )
]

month = datetime.now().month
print("The current month is {0}.".format(month))
if month == 12:
  print("Let's celebrate with holiday patterns!")
  pattern_factories = HOLIDAY_PATTERNS
else:
  pattern_factories = REGULAR_PATTERNS

application_factory.create_application(
  command_line_args=sys.argv,
  num_leds=NUM_LEDS,
  brightness_schedule=AlwaysMaxBrightnessSchedule(1.0),
  transition_length=5,
  pattern_factories=pattern_factories
).run()
