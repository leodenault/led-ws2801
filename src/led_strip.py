import Adafruit_GPIO.SPI as SPI
import Adafruit_WS2801


class LedDirection:
    """Enum class for defining directions to output light patterns on an LED
    strip connected to a Raspberry Pi.
    """

    START_TO_END = 0
    """Output patterns so that 
        the first pixel in the pattern matches with the first physical LED on 
        the strip.
    """
    END_TO_START = 1
    """Output patterns so that 
        the first pixel in the pattern matches with the last physical LED on 
        the strip
    """


class LedStrip:
    """Abstraction around a WS2801 LED strip connected to a Raspberry Pi
    through its GPIO pins and communicating through SPI.
    """

    _ALL_LEDS = -1

    def __init__(
      self,
      num_leds,
      direction=LedDirection.START_TO_END,
      spi_port=0,
      spi_device=0):
        """Creates an LedStrip object for communicating with an LED strip 
        connected to the Raspberry Pi.
        
        :param num_leds: the number of LEDs on the strip.
        :param direction: the direction in which animations should be 
        rendered. Use LedDirection.START_TO_END to output patterns so that 
        the first pixel in the pattern matches with the first physical LED on 
        the strip. Use LedDirection.END_TO_START to output patterns so that 
        the first pixel in the pattern matches the last physical LED on the 
        strip.
        :param spi_port: the SPI port to output to. Defaults to 0.
        :param spi_device: the SPI device to output to. For example, 
        specifying a device of 1 will use /dev/spidev0.1. Defaults to 0.
        """
        self.leds = Adafruit_WS2801.WS2801Pixels(
          num_leds, spi=SPI.SpiDev(spi_port, spi_device))
        self.direction = direction
        self.num_leds = num_leds

    def display(self, colour, led=_ALL_LEDS):
        """Displays a specific colour on a specific LED.

        :param colour: the colour to output to the LED.
        :param led: the index of the LED to output the colour to. If
        unspecified, then colour is displayed on all LEDs.
        """

        if led == LedStrip._ALL_LEDS:
            for i in range(0, self.num_leds):
                self.leds.set_pixel_rgb(i, colour.r, colour.g, colour.b)
        else:
            led = led if self.direction else self.num_leds - led - 1
            self.leds.set_pixel_rgb(led, colour.r, colour.g, colour.b)
        self.leds.show()

    def clear(self):
        """Clears the LED strip of any colours currently displayed.
        """

        self.leds.clear()
        self.leds.show()
