# Animates random patterns on a WS2801 LED strip with traditional holiday
# colours.

import random
import time

from colour import led_colour
from colour.cubic_interpolation import CubicInterpolation
from led_strip.led_strip import LedStrip
from led_strip.regular_brightness_schedule import RegularBrightnessSchedule
from led_strip.led_strip import LedDirection

strip = LedStrip(86, RegularBrightnessSchedule(7, 9, 4, 9, 0.1, 1.0),
  LedDirection.END_TO_START)


def compare(colour1, colour2, colours):
    return colours.index(colour1) < colours.index(colour2)


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


def assign_random_leds(colours, period):
    # Create a random array of colours the length of the strip.
    strip_colours = []
    for i in range(0, strip.num_leds):
        colour = colours[random.randint(0, len(colours) - 1)]
        strip_colours.append(colour)
        strip.set_colour_and_display(colour, i)
        time.sleep(period)
    return strip_colours


def celebrate_sort_success(
  strip_colours,
  num_celebration_flashes,
  celebration_period):
    strength_per_second = 2.0 / celebration_period
    for flash_index in range(0, num_celebration_flashes):
        strength = -1.0
        while strength < 1.0:
            start_time = time.time()
            for colour_index in range(0, len(strip_colours)):
                strip.set_colour(
                  strip_colours[colour_index].multiply(abs(strength)),
                  colour_index)
            strip.display()
            elapsed_time = time.time() - start_time
            strength += elapsed_time * strength_per_second


def merge_sort(
  colours,
  assignment_period,
  sort_period,
  celebration_period,
  num_celebration_flashes):
    print("Starting merge sort!")
    strip_colours = assign_random_leds(colours, assignment_period)
    recursive_merge_sort(
      colours, strip_colours, 0, len(strip_colours) - 1, sort_period)
    celebrate_sort_success(
      strip_colours, num_celebration_flashes, celebration_period)


def recursive_merge_sort(
  colours,
  strip_colours,
  start_index,
  end_index,
  period):
    if start_index == end_index:
        return [strip_colours[start_index]]
    else:
        num_leds = end_index - start_index + 1
        middle = start_index + num_leds / 2
        merged_left = recursive_merge_sort(
          colours, strip_colours, start_index, middle - 1, period)
        merged_right = recursive_merge_sort(
          colours, strip_colours, middle, end_index, period)

        # Merge both sides together.
        i = 0
        j = 0
        num_merged_left = len(merged_left)
        num_merged_right = len(merged_right)
        k = start_index
        while k <= end_index:
            if i == num_merged_left:
                strip_colours[k] = merged_right[j]
                j += 1
            elif j == num_merged_right:
                strip_colours[k] = merged_left[i]
                i += 1
            else:
                from_left = compare(merged_left[i], merged_right[j], colours)
                if from_left:
                    strip_colours[k] = merged_left[i]
                    i += 1
                else:
                    strip_colours[k] = merged_right[j]
                    j += 1
            k += 1

        # Create temporary array with newly merged set and display the
        # colours to
        # the strip.
        merged_all = []
        i = start_index
        while i <= end_index:
            merged_all.append(strip_colours[i])
            if strip.get_colour_at(i) != strip_colours[i]:
                strip.set_colour_and_display(strip_colours[i], i)
                time.sleep(period)
            i += 1
        return merged_all


def bubble_sort(
  colours,
  assignment_period,
  sort_period,
  celebration_period,
  num_celebration_flashes):
    print("Starting bubble sort!")
    strip_colours = assign_random_leds(colours, assignment_period)
    colours_sorted = False
    while not colours_sorted:
        colours_sorted = True
        for i in range(0, len(strip_colours) - 1):
            if compare(strip_colours[i + 1], strip_colours[i], colours):
                left = strip_colours[i]
                strip_colours[i] = strip_colours[i + 1]
                strip_colours[i + 1] = left
                strip.set_colour(strip_colours[i], i)
                strip.set_colour(strip_colours[i + 1], i + 1)
                strip.display()
                time.sleep(sort_period)
                colours_sorted = False
    celebrate_sort_success(
      strip_colours, num_celebration_flashes, celebration_period)


def snow(duration, period, spawn_rate):
    print("Starting snow!")
    start_time = time.time()
    strip.clear()
    snowflakes = []

    while time.time() - start_time < duration:
        num_snowflakes = len(snowflakes)
        for i in range(0, num_snowflakes):
            snowflake_pixel = snowflakes[i]
            strip.set_colour(led_colour.BLACK, snowflake_pixel)
            snowflakes[i] += 1

        if (num_snowflakes > 0
          and snowflakes[num_snowflakes - 1] >= strip.num_leds):
            snowflakes.pop(num_snowflakes - 1)
            num_snowflakes -= 1

        new_snowflake = (
          0 not in snowflakes
          and 1 not in snowflakes
          and random.random() > 1 - spawn_rate)
        if new_snowflake:
            snowflakes.insert(0, 0)
            num_snowflakes += 1

        for i in range(0, num_snowflakes):
            snowflake_pixel = snowflakes[i]
            strip.set_colour(led_colour.WHITE, snowflake_pixel)
        strip.display()
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
    lambda duration:
    merge_sort(
      [led_colour.WHITE, led_colour.RED, led_colour.GREEN, led_colour.GOLD],
      0.05,
      0.08,
      1.5,
      5),
    lambda duration:
    bubble_sort(
      [led_colour.WHITE, led_colour.RED, led_colour.GREEN, led_colour.GOLD],
      0.05,
      0.02,
      1.5,
      5),
    lambda duration: snow(duration, 0.2, 0.1),
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
