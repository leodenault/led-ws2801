# Animates random patterns on a WS2801 LED strip with traditional holiday
# colours.

import random
import time

from colour import led_colour
from colour.cubic_interpolation import CubicInterpolation
from led_strip.led_strip import LedDirection
from led_strip.led_strip import LedStrip
from led_strip.regular_brightness_schedule import RegularBrightnessSchedule
from pattern.snow_pattern import SnowPattern
from pattern.sorting.bubble_sort_pattern import BubbleSortPattern
from pattern.sorting.merge_sort_pattern import MergeSortPattern
from pattern.sorting.colour_distributor import ColourDistributor
from pattern.sorting.sort_celebration import SortCelebration

strip = LedStrip(
  86,
  RegularBrightnessSchedule(7, 9, 16, 21, 0.1, 1.0),
  LedDirection.END_TO_START)


def stream(colours, period, duration):
    print(
        "Starting stream with colours [{0}]!".format(
          ", ".join(str(c) for c in colours)))
    shift = 0
    num_colours = len(colours)
    start_time = time.time()
    while time.time() - start_time < duration:
        for i in range(strip.num_leds):
            colour_index = i % num_colours
            shifted_colour = (colour_index + shift) % num_colours
            strip.set_colour(colours[shifted_colour], i)
        strip.display()
        shift = (shift + 1) % num_colours
        time.sleep(period)


def distance_to_colour(index, colour_position, moving_right):
    distance = (
        colour_position - index if moving_right else index - colour_position)
    if distance < 0:
        distance = strip.num_leds + distance
    return distance


def smoothbow(colours, period, increment, duration, interpolation_mode):
    print("Starting smoothbow!")
    num_segments = len(colours)
    segment_length = strip.num_leds / float(num_segments)
    colour_positions = {}
    for i in range(0, num_segments):
        colour_positions[colours[i]] = i * segment_length

    start_time = time.time()
    while time.time() - start_time < duration:
        for i in range(0, strip.num_leds):
            nearest_colours = []
            for j in range(0, num_segments):
                right_distance = distance_to_colour(
                  i, colour_positions[colours[j]], True)
                left_distance = distance_to_colour(
                  i, colour_positions[colours[j]], False)
                if right_distance < segment_length:
                    nearest_colours.append((colours[j], right_distance, True))
                elif left_distance < segment_length:
                    nearest_colours.append((colours[j], left_distance, False))

            # At this point there should be at most 2 colours.
            num_nearest_colours = len(nearest_colours)
            if num_nearest_colours == 1:
                strip.set_colour(nearest_colours[0][0], i)
            elif num_nearest_colours == 2:
                strip.set_colour(interpolation_mode.interpolate(
                  nearest_colours[0][0],
                  nearest_colours[1][0],
                  1 - (nearest_colours[0][1] / segment_length)), i)
            else:
                print("Detected {0} nearest colours. Expected 1 or 2."
                      .format(num_nearest_colours))

        for i in range(0, num_segments):
            colour_positions[colours[i]] = (
              (colour_positions[colours[i]] + increment) % strip.num_leds)
        strip.display()
        time.sleep(period)


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

# Start up the app.
algorithms = [
    lambda duration:
    stream(
      [led_colour.WHITE, led_colour.RED, led_colour.GREEN, led_colour.GOLD],
      0.15,
      duration),
    lambda duration:
    stream(
      [led_colour.WHITE, led_colour.RED, led_colour.GREEN, led_colour.BLUE],
      0.15,
      duration),
    lambda duration:
    stream(
      [led_colour.WHITE, led_colour.RED, led_colour.GREEN, led_colour.BLUE,
          led_colour.GOLD],
      0.15,
      duration),
    lambda duration: stream([led_colour.WHITE, led_colour.RED], 0.25, duration),
    lambda duration: stream([led_colour.GREEN, led_colour.RED], 0.25, duration),
    lambda duration: stream([led_colour.GOLD, led_colour.RED], 0.25, duration),
    lambda duration: stream([led_colour.GREEN, led_colour.WHITE], 0.25,
      duration),
    lambda duration: merge_sort_pattern.animate(
      strip,
      [led_colour.WHITE, led_colour.RED, led_colour.GREEN, led_colour.GOLD]),
    lambda duration: bubble_sort_pattern.animate(
      strip,
      [led_colour.WHITE, led_colour.RED, led_colour.GREEN, led_colour.GOLD]),
    lambda duration: snow_pattern.animate(strip, [led_colour.WHITE]),
    lambda duration:
    smoothbow(
      [led_colour.WHITE.multiply(0.25), led_colour.RED, led_colour.GOLD,
          led_colour.GREEN],
      0,
      0.25,
      duration,
      CubicInterpolation())
]

# Clear all the pixels to turn them off.
strip.clear()

while True:
    algorithms[random.randint(0, len(algorithms) - 1)](random.randint(20, 40))

# Not used but you can also read pixel colors with the get_pixel_rgb function:
# r, g, b = pixels.get_pixel_rgb(0)  # Read pixel 0 red, green, blue value.
