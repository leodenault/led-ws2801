"""Factory methods for creating an Application object.
"""
from application import Application
from display.led_strip import LedDirection


def create_application(
  command_line_args,
  num_leds,
  brightness_schedule,
  transition_length,
  pattern_factories,
  direction=LedDirection.START_TO_END):
    """Creates an Application instance.

    This factory method naively parses the command line parameters to detect
    whether an Adafruit or Tkinter device should be used.

    To ensure that your application functions correctly when instantiating
    using an Adafruit device, please make sure to install the Adafruit
    controller by following the installation instructions at
    https://github.com/adafruit/Adafruit_Python_WS2801.

    To ensure that your application functions correctly when instantiating
    using an Tkinter device, please make sure to install the Tkinter on your
    system.

    :param command_line_args: the command line arguments to the program as
    formatted in sys.argv.
    :param num_leds: the number of LEDs on the device.
    :param brightness_schedule: the BrightnessSchedule used to control the
    brightness of the LEDs.
    :param transition_length: the length of time, in seconds,
    for a transition to execute.
    :param pattern_factories: the set of lambdas which will instantiate the
    desired patterns.
    :param direction: the LedDirection to use when displaying the colours on
    the LEDs.
    :return: a runnable application instance.
    """
    if "--device=tkinter" in command_line_args:
        from display.tkinter import tkinter_led_strip_factory
        return Application(
          tkinter_led_strip_factory.create_tkinter_led_strip(
            num_leds,
            brightness_schedule,
            direction),
          transition_length,
          pattern_factories)
    else:
        from display.adafruit_ws2801 import adafruit_led_strip_factory
        return Application(
          adafruit_led_strip_factory.create_adafruit_led_strip(
            num_leds,
            brightness_schedule,
            direction),
          transition_length,
          pattern_factories)
