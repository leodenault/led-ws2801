import time


class SortCelebration:
    """Configuration for celebrating the end of a sorting pattern.
    """

    def __init__(self, num_celebration_flashes, celebration_flash_duration):
        """Creates a SortCelebration configuration.

        :param num_celebration_flashes: the number of times the LEDs should
        flash in celebration.
        :param celebration_flash_duration: the amount of time, in seconds,
        it should take for a single flash to occur.
        """

        self.num_celebration_flashes = num_celebration_flashes
        self.celebration_flash_duration = celebration_flash_duration

    def celebrate(self, leds, strip_colours):
        """Celebrates the end of a sorting pattern by flashing.

        :param leds: the LedStrip reference used for communicating with the
        physical LED strip.
        :param strip_colours: an array of colours to be assigned to the LED
        strip. Its size must be the same as the number of LEDs on the strip.
        """

        strength_per_second = 2.0 / self.celebration_flash_duration
        for flash_index in range(0, self.num_celebration_flashes):
            strength = -1.0
            while strength < 1.0:
                start_time = time.time()
                for colour_index in range(0, len(strip_colours)):
                    leds.set_colour(
                      strip_colours[colour_index].multiply(abs(strength)),
                      colour_index)
                leds.display()
                elapsed_time = time.time() - start_time
                strength += elapsed_time * strength_per_second
