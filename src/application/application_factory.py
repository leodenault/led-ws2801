"""Factory methods for creating an Application object using an underlying
Adafruit WS2801 controller.

To ensure that your application functions correctly, please make sure to
install the Adafruit controller by
following the installation instructions at
https://github.com/adafruit/Adafruit_Python_WS2801.
"""
from application import Application
from display.led_strip import LedDirection


def create_application(
  args,
  num_leds,
  brightness_schedule,
  pattern_factories,
  direction=LedDirection.START_TO_END):
    if "--device=tkinter" in args:
        from display.tkinter import tkinter_led_strip_factory
        return Application(
          tkinter_led_strip_factory.create_tkinter_led_strip(
            num_leds,
            brightness_schedule,
            direction),
          pattern_factories)
    else:
        from display.adafruit_ws2801 import adafruit_led_strip_factory
        return Application(
          adafruit_led_strip_factory.create_adafruit_led_strip(
            num_leds,
            brightness_schedule,
            direction),
          pattern_factories)
