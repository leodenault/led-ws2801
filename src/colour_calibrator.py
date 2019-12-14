"""Displays colours on the LED strip through the command line.
"""

import sys

from colour.led_colour import Colour
from display.brightness.always_max_brightness_schedule import \
  AlwaysMaxBrightnessSchedule

num_leds = 0
r = 255
g = 255
b = 255
brightness_schedule = AlwaysMaxBrightnessSchedule(1.0)
keep_displaying = False


def parse_int_arg(arg):
  int_arg = arg.partition("=")[2]
  try:
    return int(int_arg)
  except:
    return 0


def parse_colour_component(arg):
  colour_component = parse_int_arg(arg)
  if colour_component > 255:
    return 255
  elif colour_component < 0:
    return 0
  return colour_component


for arg in sys.argv:
  if arg.startswith("--num_leds="):
    num_leds = parse_int_arg(arg)
  elif arg.startswith("--r="):
    r = parse_colour_component(arg)
  elif arg.startswith("--g="):
    g = parse_colour_component(arg)
  elif arg.startswith("--b="):
    b = parse_colour_component(arg)

is_adafruit = False
if "--device=tkinter" in sys.argv:
  from display.tkinter import tkinter_led_strip_factory

  device = (
    tkinter_led_strip_factory.create_tkinter_led_strip(num_leds,
                                                       brightness_schedule))
  keep_displaying = True
else:
  from display.adafruit_ws2801 import adafruit_led_strip_factory

  device = adafruit_led_strip_factory.create_adafruit_led_strip(
    num_leds,
    brightness_schedule)
  is_adafruit = True

device.set_colour(Colour(r, g, b))
device.display()

if is_adafruit:
  exit()

while device.is_active():
  pass
