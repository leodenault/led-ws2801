import math

from display.led_strip import DrawingMode
from pattern.renderable.renderable import Renderable


class Spotlight(Renderable):
    """A simple light that shines brightest at its position and that
    diminishes in further LEDs.
    """

    def __init__(self, position, colour, radius):
        """Creates a spotlight renderable object.

        :param position: the initial position of the center of the spotlight.
        :param colour: the colour that the spotlight should display.
        :param radius: the distance from the center from which the light
        radiates.
        """
        self.position = position
        self.colour = colour
        self.radius = radius
        self.brightness_function_factor = -1.0 / (radius * radius)

    def render(self, leds):
        previous_drawing_mode = leds.get_drawing_mode()
        leds.set_drawing_mode(DrawingMode.BLEND)

        if self.position % 1 == 0:
            leds.set_colour(self.colour, int(self.position))

        for i in range(1, self.radius + 1):
            num_leds = leds.get_num_leds()
            left_position = int(math.ceil(self.position - i))
            right_position = int(math.floor(self.position + i))

            leds.set_colour(
              self.colour.multiply(
                self._compute_brightness(left_position - self.position)),
              left_position % num_leds)
            leds.set_colour(
              self.colour.multiply(
                self._compute_brightness(right_position - self.position)),
              right_position % num_leds)

        leds.set_drawing_mode(previous_drawing_mode)

    def setPosition(self, position):
        self.position = position

    def _compute_brightness(self, x):
        return self.brightness_function_factor * x * x + 1
