import time

from sort_pattern import SortPattern, compare


class BubbleSortPattern(SortPattern):
    """A pattern which sorts colours randomly assigned to the LEDs on a strip 
    using the bubble sort algorithm.
    """

    def sort(self, leds, colour_palette, strip_data):
        colours_sorted = False
        while not colours_sorted:
            colours_sorted = True
            for i in range(0, len(strip_data) - 1):
                if compare(strip_data[i + 1], strip_data[i], colour_palette):
                    left = strip_data[i]
                    strip_data[i] = strip_data[i + 1]
                    strip_data[i + 1] = left
                    leds.set_colour(strip_data[i], i)
                    leds.set_colour(strip_data[i + 1], i + 1)
                    leds.display()
                    time.sleep(self.sort_step_duration)
                    colours_sorted = False
