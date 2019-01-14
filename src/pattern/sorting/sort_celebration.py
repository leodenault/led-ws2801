from pattern.pattern import Pattern


class SortCelebration(Pattern):
    """Configuration for celebrating the end of a sorting pattern.
    """

    def __init__(
      self, num_celebration_flashes, celebration_flash_duration, strip_data):
        """Creates a SortCelebration configuration.

        :param num_celebration_flashes: the number of times the LEDs should
        flash in celebration.
        :param celebration_flash_duration: the amount of time, in seconds,
        it should take for a single flash to occur.
        :param strip_data: the colour data displayed on the LED strip before
        beginning this pattern, expressed as an array of Colours.
        """

        self.num_celebration_flashes = num_celebration_flashes
        self.progress_per_second = 2.0 / celebration_flash_duration
        self.current_flash_index = 0
        self.flash_progress = 0
        self.strip_data = strip_data

    def update(self, leds, delta):
        if self.is_done():
            return

        self.flash_progress += delta * self.progress_per_second
        if self.flash_progress >= 1:
            self.flash_progress = -1
            self.current_flash_index += 1

        if self.is_done():
            return

        for i in range(0, len(self.strip_data)):
            leds.set_colour(
              self.strip_data[i].multiply(abs(self.flash_progress)), i)

    def is_done(self):
        return self.current_flash_index >= self.num_celebration_flashes
