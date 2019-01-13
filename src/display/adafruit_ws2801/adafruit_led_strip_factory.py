"""Factory methods for creating an LedStrip object using an underlying
Adafruit WS2801 controller.

To ensure that your application functions correctly, please make sure to
install the Adafruit controller by
following the installation instructions at
https://github.com/adafruit/Adafruit_Python_WS2801.
"""

from display.adafruit_ws2801.adafruit_ws2801_led_strip_controller_adapter \
    import \
    AdafruitWs2801LedStripControllerAdapter
from display.led_strip import LedDirection, LedStrip


def create_adafruit_led_strip(
  num_leds,
  brightness_schedule,
  direction=LedDirection.START_TO_END,
  spi_port=0,
  spi_device=0):
    """Creates an LedStrip instance using the Adafruit WS2801 controller as
    its device.

    :param num_leds: the number of LEDs on the strip.
    :param brightness_schedule: the BrightnessSchedule object configuring
    how bright the LEDs should be depending on the time of day.
    :param direction: the direction in which animations should be
    rendered. Use LedDirection.START_TO_END to output patterns so that
    the first pixel in the pattern matches with the first physical LED on
    the strip. Use LedDirection.END_TO_START to output patterns so that
    the first pixel in the pattern matches the last physical LED on the
    strip.
    :param spi_port: the SPI port to output to. Defaults to 0.
    :param spi_device: the SPI device to output to. For example, specifying a
    device of 1 will use /dev/spidev0.1. Defaults to 0.
    :return: an LedStrip object for interacting with the physical strip.
    """
    return LedStrip(
      AdafruitWs2801LedStripControllerAdapter(num_leds, spi_port, spi_device),
      brightness_schedule,
      direction)
