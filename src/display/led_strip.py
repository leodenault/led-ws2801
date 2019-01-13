class LedDirection:
    """Enum class for defining directions to output light patterns on an LED
    strip connected to a Raspberry Pi.
    """

    START_TO_END = 0
    """Output patterns so that the first pixel in the pattern matches with
    the first physical LED on the strip.
    """
    END_TO_START = 1
    """Output patterns so that the first pixel in the pattern matches with
    the last physical LED on the strip.
    """


class LedStrip:
    """Abstraction around a WS2801 LED strip connected to a Raspberry Pi
    through its GPIO pins and communicating through SPI.
    """

    _ALL_LEDS = -1

    def __init__(
      self,
      device,
      brightness_schedule,
      direction=LedDirection.START_TO_END):
        """Creates an LedStrip object for communicating with an LED strip 
        connected to the Raspberry Pi.

        :param device: the specific Device instance that controls the LED strip.
        :param brightness_schedule: the BrightnessSchedule object configuring
        how bright the LEDs should be depending on the time of day.
        :param direction: the direction in which animations should be
        rendered. Use LedDirection.START_TO_END to output patterns so that 
        the first pixel in the pattern matches with the first physical LED on 
        the strip. Use LedDirection.END_TO_START to output patterns so that 
        the first pixel in the pattern matches the last physical LED on the 
        strip.
        """
        self.device = device
        self.brightness_schedule = brightness_schedule
        self.direction = direction

    def set_colour(self, colour, led=_ALL_LEDS):
        """Sets the colour of one or all LEDs on a strip.

        :param colour: the colour to output to the LED.
        :param led: the index of the LED to output the colour to. If
        unspecified, then colour is displayed on all LEDs.
        """

        brightness = self.brightness_schedule.get_brightness()
        displayed_colour = colour.multiply(brightness)

        if led == LedStrip._ALL_LEDS:
            for i in range(0, self.device.get_num_leds()):
                self.device.set_led_colour(i, displayed_colour)
        else:
            self.device.set_led_colour(
              self._fetch_physical_index(led), displayed_colour)

    def set_colour_and_display(self, colour, led=_ALL_LEDS):
        """Sets the colour of one or all LEDs on a strip and then displays it.

        :param colour: the colour to output to the LED.
        :param led: the index of the LED to output the colour to. If
        unspecified, then colour is displayed on all LEDs.
        """
        self.set_colour(colour, led)
        self.device.show()

    def display(self):
        """Displays the colours currently assigned to the LEDs.
        """
        self.device.show()

    def clear(self):
        """Clears the LED strip of any colours currently displayed.
        """

        self.device.clear()
        self.device.show()

    def _fetch_physical_index(self, logical_index):
        return (
            logical_index if self.direction == LedDirection.START_TO_END else
            self.device.get_num_leds() - logical_index - 1)

    def get_num_leds(self):
        return self.device.get_num_leds()
