import Adafruit_GPIO.SPI as SPI
import Adafruit_WS2801

from display.device import Device


class AdafruitWs2801LedStripControllerAdapter(Device):
    """Adapter class which integrates with the Adafruit LED controller library.

    To ensure that your application functions correctly, please make sure to
    follow the installation instructions at
    https://github.com/adafruit/Adafruit_Python_WS2801.
    """

    def __init__(self, num_leds, spi_port, spi_device):
        """Instantiates an Adafruit WS 2801 LED strip controller adapter.

        :param num_leds: the number of LEDs on the strip.
        :param spi_port: the SPI port to output to.
        :param spi_device: the SPI device to output to. For example,
        specifying a device of 1 will use /dev/spidev0.1.
        """
        self.controller = Adafruit_WS2801.WS2801Pixels(
          num_leds, spi=SPI.SpiDev(spi_port, spi_device))
        self.num_leds = num_leds

    def set_led_colour(self, index, colour):
        self.controller.set_pixel_rgb(index, colour.r, colour.g, colour.b)

    def show(self):
        self.controller.show()

    def clear(self):
        self.controller.clear()

    def get_num_leds(self):
        return self.num_leds


