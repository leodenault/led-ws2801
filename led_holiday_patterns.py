# Animates random patterns on a WS2801 LED strip with traditional holiday
# colours.

import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

from led_colour import Colour

import random
import time
from datetime import datetime

# Configure the count of pixels:
PIXEL_COUNT = 86

# Configure whether the LEDs should iterate from start-to-end or vice-versa.
START_TO_END = False

# Specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT = 0
SPI_DEVICE = 0
PIXELS = Adafruit_WS2801.WS2801Pixels(
  PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Brightness adjustment by time of day.
RAMP_UP_HOUR_START = 7
RAMP_UP_MINUTE_START = RAMP_UP_HOUR_START * 60
RAMP_UP_HOUR_END = 9
RAMP_UP_DURATION_MINUTES = (RAMP_UP_HOUR_END - RAMP_UP_HOUR_START) * 60
RAMP_DOWN_HOUR_START = 16
RAMP_DOWN_MINUTE_START = RAMP_DOWN_HOUR_START * 60
RAMP_DOWN_HOUR_END = 21
RAMP_DOWN_DURATION_MINUTES = (RAMP_DOWN_HOUR_END - RAMP_DOWN_HOUR_START) * 60
MAX_BRIGHTNESS = 1.0
MIN_BRIGHTNESS = 0.1
BRIGHTNESS_DELTA = MAX_BRIGHTNESS - MIN_BRIGHTNESS


class InterpolationMode:
    LINEAR = 1
    QUADRATIC = 2
    CUBIC = 3


# Breaks if the ramp up or down times cross a daily border.
def brightness_factor():
    current_time = datetime.now().time()
    current_hour = current_time.hour
    if current_hour < RAMP_UP_HOUR_START or current_hour >= RAMP_DOWN_HOUR_END:
        return MIN_BRIGHTNESS
    if RAMP_UP_HOUR_END <= current_hour < RAMP_DOWN_HOUR_START:
        return MAX_BRIGHTNESS

    minute_of_day = current_hour * 60.0 + current_time.minute
    if current_hour < RAMP_UP_HOUR_END:
        completion = (
          (minute_of_day - RAMP_UP_MINUTE_START) / RAMP_UP_DURATION_MINUTES)
        return completion * BRIGHTNESS_DELTA + MIN_BRIGHTNESS

    completion = (
      (minute_of_day - RAMP_DOWN_MINUTE_START) / RAMP_DOWN_DURATION_MINUTES)
    return (1 - completion) * BRIGHTNESS_DELTA + MIN_BRIGHTNESS


def display(pixels, led, colour):
    led = led if START_TO_END else PIXEL_COUNT - led - 1
    dimmed_colour = colour.multiply(brightness_factor())
    pixels.set_pixel_rgb(led, dimmed_colour.r, dimmed_colour.g, dimmed_colour.b)


def compare(colour1, colour2, colours):
    return colours.index(colour1) < colours.index(colour2)


def stream(colours, period, duration):
    print(
        "Starting stream with colours [{0}]!"
            .format(", ".join(str(c) for c in colours)))
    shift = 0
    num_colours = len(colours)
    start_time = time.time()
    while (time.time() - start_time < duration):
        for i in range(PIXEL_COUNT):
            colour_index = i % num_colours
            shifted_colour = (colour_index + shift) % num_colours
            display(PIXELS, i, colours[shifted_colour])
        PIXELS.show()
        shift = (shift + 1) % num_colours
        time.sleep(period)


def assign_random_leds(colours, period):
    # Create a random array of colours the length of the strip.
    strip_colours = []
    for i in range(0, PIXEL_COUNT):
        led_colour = colours[random.randint(0, len(colours) - 1)]
        strip_colours.append(led_colour)
        display(PIXELS, i, led_colour)
        PIXELS.show()
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
                display(
                  PIXELS,
                  colour_index,
                  strip_colours[colour_index].multiply(abs(strength)))
            PIXELS.show()
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
    if (start_index == end_index):
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
        while (k <= end_index):
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
        while (i <= end_index):
            merged_all.append(strip_colours[i])
            if PIXELS.get_pixel_rgb(i) != strip_colours[i]:
                display(PIXELS, i, strip_colours[i])
                PIXELS.show()
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
                display(PIXELS, i, strip_colours[i])
                display(PIXELS, i + 1, strip_colours[i + 1])
                PIXELS.show()
                time.sleep(sort_period)
                colours_sorted = False
    celebrate_sort_success(
      strip_colours, num_celebration_flashes, celebration_period)


def snow(duration, period, spawn_rate, dim_factor):
    print("Starting snow!")
    start_time = time.time()
    PIXELS.clear()
    PIXELS.show()
    snowflakes = []

    while time.time() - start_time < duration:
        num_snowflakes = len(snowflakes)
        for i in range(0, num_snowflakes):
            snowflake_pixel = snowflakes[i]
            display(PIXELS, snowflake_pixel, Colour.BLACK)
            snowflakes[i] += 1

        if num_snowflakes > 0 and snowflakes[num_snowflakes - 1] >= PIXEL_COUNT:
            snowflakes.pop(num_snowflakes - 1)
            num_snowflakes -= 1

        new_snowflake = (
          0 not in snowflakes
          and 1 not in snowflakes
          and random.random() > 1 - spawn_rate)
        if (new_snowflake):
            snowflakes.insert(0, 0)
            num_snowflakes += 1

        for i in range(0, num_snowflakes):
            snowflake_pixel = snowflakes[i]
            display(PIXELS, snowflake_pixel, Colour.WHITE)
        PIXELS.show()
        time.sleep(period)


def distance_to_colour(index, colour_position, moving_right):
    distance = (
        colour_position - index if moving_right else index - colour_position)
    if distance < 0:
        distance = PIXEL_COUNT + distance
    return distance


def interpolate(colour1, colour2, distance_to_colour1, segment_length, mode):
    factor1 = 1 - (distance_to_colour1 / segment_length)
    factor2 = 1 - factor1

    if mode == InterpolationMode.QUADRATIC:
        factor1 *= factor1
        factor2 *= factor2
    if mode == InterpolationMode.CUBIC:
        factor1 *= factor1 * factor1
        factor2 *= factor2 * factor2

    return colour1.multiply(factor1).add(colour2.multiply(factor2))


def smoothbow(colours, period, increment, duration, interpolation_mode):
    print("Starting smoothbow!")
    num_segments = len(colours)
    segment_length = PIXEL_COUNT / float(num_segments)
    colour_positions = {}
    for i in range(0, num_segments):
        colour_positions[colours[i]] = i * segment_length

    start_time = time.time()
    while time.time() - start_time < duration:
        for i in range(0, PIXEL_COUNT):
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
                display(PIXELS, i, nearest_colours[0][0])
            elif num_nearest_colours == 2:
                display(
                  PIXELS,
                  i,
                  interpolate(
                    nearest_colours[0][0],
                    nearest_colours[1][0],
                    nearest_colours[0][1],
                    segment_length,
                    interpolation_mode))
            else:
                print("Detected {0} nearest colours. Expected 1 or 2."
                      .format(num_nearest_colours))

        for i in range(0, num_segments):
            colour_positions[colours[i]] = (
              (colour_positions[colours[i]] + increment) % PIXEL_COUNT)
        PIXELS.show()
        time.sleep(period)


# Start up the app.
algorithms = [
    lambda duration:
    stream(
      [Colour.WHITE, Colour.RED, Colour.GREEN, Colour.GOLD],
      0.15,
      duration),
    lambda duration:
    stream(
      [Colour.WHITE, Colour.RED, Colour.GREEN, Colour.BLUE],
      0.15,
      duration),
    lambda duration:
    stream(
      [Colour.WHITE, Colour.RED, Colour.GREEN, Colour.BLUE, Colour.GOLD],
      0.15,
      duration),
    lambda duration: stream([Colour.WHITE, Colour.RED], 0.25, duration),
    lambda duration: stream([Colour.GREEN, Colour.RED], 0.25, duration),
    lambda duration: stream([Colour.GOLD, Colour.RED], 0.25, duration),
    lambda duration: stream([Colour.GREEN, Colour.WHITE], 0.25, duration),
    lambda duration:
    merge_sort(
      [Colour.WHITE, Colour.RED, Colour.GREEN, Colour.GOLD],
      0.05,
      0.08,
      1.5,
      5),
    lambda duration:
    bubble_sort(
      [Colour.WHITE, Colour.RED, Colour.GREEN, Colour.GOLD],
      0.05,
      0.02,
      1.5,
      5),
    lambda duration: snow(duration, 0.2, 0.1, 0.05),
    lambda duration:
    smoothbow(
      [Colour.WHITE.multiply(0.25), Colour.RED, Colour.GOLD, Colour.GREEN],
      0,
      0.25,
      duration,
      InterpolationMode.QUADRATIC)
]

# Clear all the pixels to turn them off.
PIXELS.clear()
PIXELS.show()  # Make sure to call show() after changing any pixels!

while (True):
    algorithms[random.randint(0, len(algorithms) - 1)](random.randint(20, 40))

# Not used but you can also read pixel colors with the get_pixel_rgb function:
# r, g, b = pixels.get_pixel_rgb(0)  # Read pixel 0 red, green, blue value.
