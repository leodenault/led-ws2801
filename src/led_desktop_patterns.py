"""Animates random patterns on a WS2801 LED strip mounted on desktop furniture
for an aesthetically pleasing effect.
"""

import random
import sys
from datetime import datetime

from application import application_factory
from colour import led_colour, palette
from colour.cubic_interpolation import CubicInterpolation
from colour.led_colour import Colour
from colour.linear_interpolation import LinearInterpolation
from display.brightness.always_max_brightness_schedule import \
  AlwaysMaxBrightnessSchedule
from pattern import stream_pattern
from pattern.pulsing_pattern import PulsingPattern
from pattern.stream_pattern import StreamPattern
from pattern.swinging_spotlight_pattern import SwingingSpotlightPattern
from pattern.twinkle_pattern import TwinklePattern

NUM_LEDS = 71
MIN_PULSE_PERIOD = 5
MAX_PULSE_PERIOD = 10
MIN_STREAM_PERIOD = 8
MAX_STREAM_PERIOD = 30
MIN_STREAM_SEGMENTS = 3
MAX_STREAM_SEGMENTS = 20
MIN_STREAM_COLOUR_LENGTH = int(NUM_LEDS / MAX_STREAM_SEGMENTS)
MAX_STREAM_COLOUR_LENGTH = int(NUM_LEDS / MIN_STREAM_SEGMENTS)
MIN_TIME_BETWEEN_TWINKLES = 0.2
MAX_TIME_BETWEEN_TWINKLES = 0.5
MIN_TWINKLE_LENGTH = 1
MAX_TWINKLE_LENGTH = 5
MIN_SWINGING_SPOTLIGHT_RADIUS = 2
MAX_SWINGING_SPOTLIGHT_RADIUS = 10
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
HALLOWEEN_PATTERNS = [
  lambda:
  StreamPattern(
    num_leds=NUM_LEDS,
    period=random.randint(MIN_STREAM_PERIOD, MAX_STREAM_PERIOD),
    interpolation_mode=LinearInterpolation(),
    colour_palette=stream_pattern.create_colour_cycle([
      led_colour.VERY_DARK_RED,
      led_colour.PURPLE,
      led_colour.BLACK],
      NUM_LEDS,
      random.randint(MIN_STREAM_COLOUR_LENGTH, MAX_STREAM_COLOUR_LENGTH)),
    display_time=30
  ),
  lambda:
  StreamPattern(
    num_leds=NUM_LEDS,
    period=random.randint(MIN_STREAM_PERIOD, MAX_STREAM_PERIOD),
    interpolation_mode=LinearInterpolation(),
    colour_palette=stream_pattern.create_colour_cycle(
      palette.choose_random_from(
        [
          led_colour.DARK_GREEN,
          led_colour.PURPLE,
          led_colour.BLACK,
          led_colour.ORANGE]),
      NUM_LEDS,
      random.randint(MIN_STREAM_COLOUR_LENGTH, MAX_STREAM_COLOUR_LENGTH)),
    display_time=30
  ),
  lambda:
  SwingingSpotlightPattern(
    colour1=palette.choose_random_from(
      [led_colour.DARK_GREEN, led_colour.PURPLE, led_colour.ORANGE],
      1
    )[0],
    colour2=palette.choose_random_from(
      [led_colour.DARK_GREEN, led_colour.PURPLE, led_colour.ORANGE],
      1
    )[0],
    spotlight_radius=random.randint(MIN_SWINGING_SPOTLIGHT_RADIUS,
                                    MAX_SWINGING_SPOTLIGHT_RADIUS),
    swing_period=7.5,
    display_time=40
  )
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
    pulse_period=random.randint(MIN_PULSE_PERIOD, MAX_PULSE_PERIOD),
    display_time=30
  ),
  lambda:
  StreamPattern(
    num_leds=NUM_LEDS,
    period=random.randint(MIN_STREAM_PERIOD, MAX_STREAM_PERIOD),
    interpolation_mode=LinearInterpolation(),
    colour_palette=stream_pattern.create_colour_cycle(
      palette.choose_random_from(
        [
          led_colour.RED,
          led_colour.GOLD,
          led_colour.WHITE,
          led_colour.GREEN]),
      NUM_LEDS,
      random.randint(MIN_STREAM_COLOUR_LENGTH, MAX_STREAM_COLOUR_LENGTH)),
    display_time=30
  ),
  lambda:
  StreamPattern(
    num_leds=NUM_LEDS,
    period=random.randint(MIN_STREAM_PERIOD, MAX_STREAM_PERIOD),
    interpolation_mode=LinearInterpolation(),
    colour_palette=stream_pattern.create_colour_cycle(
      palette.choose_random_from(
        [
          led_colour.BLUE,
          led_colour.GOLD,
          led_colour.WHITE]),
      NUM_LEDS,
      random.randint(MIN_STREAM_COLOUR_LENGTH, MAX_STREAM_COLOUR_LENGTH)),
    display_time=30
  ),
  lambda:
  TwinklePattern(
    num_leds=NUM_LEDS,
    average_time_between_twinkles=(
        random.random() * MAX_TIME_BETWEEN_TWINKLES
        + MIN_TIME_BETWEEN_TWINKLES),
    twinkle_length=random.randint(MIN_TWINKLE_LENGTH, MAX_TWINKLE_LENGTH),
    display_time=30
  )
]

month = datetime.now().month
print("The current month is {0}.".format(month))
if month == 10:
  print("Let's celebrate with Halloween patterns!")
  pattern_factories = HALLOWEEN_PATTERNS
elif month == 12:
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
