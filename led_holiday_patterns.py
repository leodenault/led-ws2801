# Simple demo of of the WS2801/SPI-like addressable RGB LED lights.
# Will color all the lights different primary colors.
# Author: Tony DiCola
# License: Public Domain

# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

import random
import time

class Colour:
  def __init__(self, r, g, b, name=""):
    self.r = r
    self.g = g
    self.b = b
    self.name = name
  
  def add(self, other):
    return Colour(self.r + other.r, self.g + other.g, self.b + other.b)
  
  def multiply(self, factor):
    return Colour(int(self.r * factor), int(self.g * factor), int(self.b * factor))
  
  def __str__(self):
    if self.name:
      return self.name
    else:
      return "({0}, {1}, {2})".format(self.r, self.g, self.b)

# Configure the count of pixels:
PIXEL_COUNT = 86

# Specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT   = 0
SPI_DEVICE = 0
PIXELS = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Clear all the pixels to turn them off.
PIXELS.clear()
PIXELS.show()  # Make sure to call show() after changing any pixels!

WHITE = Colour(255, 255, 255, "White")
RED = Colour(255, 0, 0, "Red")
GREEN = Colour(0, 255, 0, "Green")
BLUE = Colour(0, 0, 255, "Blue")
BLACK = Colour(0, 0, 0, "Black")
GOLD = Colour(255, 229, 50, "Gold")

class InterpolationMode:
  LINEAR = 1
  QUADRATIC = 2
  CUBIC = 3

def display(pixels, led, colour):
  pixels.set_pixel_rgb(led, colour.r, colour.g, colour.b)

def compare(colour1, colour2, colours):
  return colours.index(colour1) < colours.index(colour2)

def stream(colours, period, duration):
  print("Starting stream with colours [{0}]!".format(", ".join(str(c) for c in colours)))
  shift = 0
  num_colours = len(colours)
  start_time = time.time()
  while(time.time() - start_time < duration):
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

def celebrate_sort_success(strip_colours, num_celebration_flashes, celebration_period):
  for i in range(num_celebration_flashes):
    for j in range(0, len(strip_colours)):
      display(PIXELS, j, BLACK)
    PIXELS.show()
    time.sleep(celebration_period)
    for j in range(0, len(strip_colours)):
      display(PIXELS, j, strip_colours[j])
    PIXELS.show()
    time.sleep(celebration_period)

def merge_sort(
    colours,
    assignment_period,
    sort_period,
    celebration_period,
    num_celebration_flashes):
  print("Starting merge sort!")
  strip_colours = assign_random_leds(colours, assignment_period)
  recursive_merge_sort(colours, strip_colours, 0, len(strip_colours) - 1, sort_period)
  celebrate_sort_success(strip_colours, num_celebration_flashes, celebration_period)  
  
def recursive_merge_sort(colours, strip_colours, start_index, end_index, period):

  if (start_index == end_index):
    return [strip_colours[start_index]]
  else:
    num_leds = end_index - start_index + 1
    middle = start_index + num_leds / 2
    merged_left = recursive_merge_sort(colours, strip_colours, start_index, middle - 1, period)
    merged_right = recursive_merge_sort(colours, strip_colours, middle, end_index, period)
    
    # Merge both sides together.
    i = 0
    j = 0
    num_merged_left = len(merged_left)
    num_merged_right = len(merged_right)
    k = start_index
    while(k <= end_index):
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
    
    # Create temporary array with newly merged set and display the colours to the strip.
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
  celebrate_sort_success(strip_colours, num_celebration_flashes, celebration_period)

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
      display(PIXELS, snowflake_pixel, BLACK)
      snowflakes[i] += 1
      
    if num_snowflakes > 0 and snowflakes[num_snowflakes - 1] >= PIXEL_COUNT:
      snowflakes.pop(num_snowflakes - 1)
      num_snowflakes -= 1
    
    new_snowflake = 0 not in snowflakes and 1 not in snowflakes and random.random() > 1 - spawn_rate
    if (new_snowflake):
      snowflakes.insert(0, 0)
      num_snowflakes += 1
    
    for i in range(0, num_snowflakes):
      snowflake_pixel = snowflakes[i]
      display(PIXELS, snowflake_pixel, WHITE)
    PIXELS.show()
    time.sleep(period)

def distance_to_colour(index, colour_position, moving_right):
  distance = colour_position - index if moving_right else index - colour_position
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
        right_distance = distance_to_colour(i, colour_positions[colours[j]], True)
        left_distance = distance_to_colour(i, colour_positions[colours[j]], False)
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
        print("Detected {0} nearest colours. Expected 1 or 2.".format(num_nearest_colours))
    
    for i in range(0, num_segments):
      colour_positions[colours[i]] = (colour_positions[colours[i]] + increment) % PIXEL_COUNT
    PIXELS.show()
    time.sleep(period)

algorithms = [
  lambda duration: stream([WHITE, RED, GREEN, BLUE], 0.15, duration),
  lambda duration: stream([WHITE, RED], 0.25, duration),
  lambda duration: stream([GREEN, RED], 0.25, duration),
  lambda duration: stream([GREEN, WHITE], 0.25, duration),
  lambda duration: merge_sort([WHITE, RED, GREEN, BLUE], 0.05, 0.08, 0.25, 5),
  lambda duration: bubble_sort([WHITE, RED, GREEN, BLUE], 0.05, 0.02, 0.25, 5),
  lambda duration: snow(duration, 0.2, 0.1, 0.05),
  lambda duration:
      smoothbow(
          [WHITE.multiply(0.25), RED, BLUE, GREEN],
          0,
          0.25,
          duration,
          InterpolationMode.QUADRATIC)
]

while(True):
  algorithms[random.randint(0, len(algorithms) - 1)](random.randint(20, 40))
  

# Not used but you can also read pixel colors with the get_pixel_rgb function:
#r, g, b = pixels.get_pixel_rgb(0)  # Read pixel 0 red, green, blue value.
