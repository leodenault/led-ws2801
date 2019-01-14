from pattern.time_interval import TimeInterval
from pattern.pattern import Pattern
import sort_patterns


class BubbleSortPattern(Pattern):
    """A pattern which sorts colours randomly assigned to the LEDs on a strip 
    using the bubble sort algorithm.
    """

    def __init__(self, colour_palette, strip_data, sort_step_duration):
        """Instantiates a BubbleSortPattern.

        :param colour_palette: the set of colours used for comparison
        operations. The order of the colours in the list is used to determine
        the outcome of a comparison.
        :param strip_data: the colour data displayed on the LED strip before
        beginning this pattern, expressed as an array of Colours.
        :param sort_step_duration: the amount of time a single step takes to
        execute.
        """
        self.colour_pallette = colour_palette
        self.strip_data = strip_data
        self.time_interval = TimeInterval(sort_step_duration)
        self.current_led = 0
        self.colours_sorted = False

    def update(self, leds, delta):
        time_exceeded = self.time_interval.time_exceeded(delta)

        if self.is_done() or not time_exceeded:
            return

        num_leds = len(self.strip_data)
        last_led = (self.current_led - 1) % (num_leds - 1)
        while self.current_led != last_led:
            compared_led = self.current_led
            self.current_led = (self.current_led + 1) % (num_leds - 1)
            swap_required = sort_patterns.compare(
              self.strip_data[compared_led + 1],
              self.strip_data[compared_led],
              self.colour_pallette)

            if swap_required:
                left = self.strip_data[compared_led]
                self.strip_data[compared_led] = self.strip_data[
                    compared_led + 1]
                self.strip_data[compared_led + 1] = left
                leds.set_colour(self.strip_data[compared_led], compared_led)
                leds.set_colour(
                  self.strip_data[compared_led + 1],
                  compared_led + 1)
                return
        self.colours_sorted = True

    def is_done(self):
        return self.colours_sorted
