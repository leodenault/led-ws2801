import sort_patterns
from pattern.pattern import Pattern
from pattern.time_interval import TimeInterval


class _SegmentContext:
    def __init__(
      self, start_index, end_index, middle, strip_data, colour_palette):
        self.start_index = start_index
        self.end_index = end_index
        self.middle = middle
        self.strip_data = strip_data
        self.colour_palette = colour_palette

    def step(self, leds):
        if self.is_merged():
            return

        while (self.start_index < self.end_index
               and sort_patterns.compare(
            self.strip_data[self.start_index],
            self.strip_data[self.middle],
            self.colour_palette)):
            self.start_index += 1

        if self.is_merged():
            return

        next_colour = self.strip_data[self.middle]
        self._shift_right(leds)
        self.strip_data[self.start_index] = next_colour
        leds.set_colour_and_display(
          self.strip_data[self.start_index], self.start_index)
        self.middle += 1
        self.start_index += 1

    def is_merged(self):
        return self.start_index == self.middle or self.middle > self.end_index

    def _shift_right(self, leds):
        for i in range(self.end_index, self.start_index, -1):
            self.strip_data[i] = self.strip_data[i - 1]
            leds.set_colour(self.strip_data[i], i)


class MergeSortPattern(Pattern):
    """A pattern which sorts colours using the merge sort algorithm.
    """

    def __init__(self, num_leds, sort_step_duration, colour_palette, strip_data):
        """Instantiates a MergeSortPattern.

        :param num_leds: the number of LEDs on the device.
        :param sort_step_duration: the amount of time a single step takes to
        execute.
        :param colour_palette: the set of colours used for comparison
        operations. The order of the colours in the list is used to determine
        the outcome of a comparison.
        :param strip_data: the colour data displayed on the LED strip before
        beginning this pattern, expressed as an array of Colours.
        """
        self.time_interval = TimeInterval(sort_step_duration)
        self.colour_palette = colour_palette
        self.strip_data = strip_data
        self.segments = []
        self._generate_segments(0, num_leds - 1, self.segments)
        self.current_segment = _SegmentContext(0, 0, 1, None, None)

    def update(self, leds, delta):
        time_exceeded = self.time_interval.time_exceeded(delta)
        if self.is_done() or not time_exceeded:
            return

        if self.current_segment.is_merged():
            self.current_segment = self.segments.pop()

        self.current_segment.step(leds)

    def is_done(self):
        return len(self.segments) == 0 and self.current_segment.is_merged()

    def _generate_segments(self, start_index, end_index, segments):
        if start_index == end_index:
            return

        num_leds = end_index - start_index + 1
        middle = start_index + num_leds / 2
        segments.append(
          _SegmentContext(
            start_index,
            end_index,
            middle,
            self.strip_data,
            self.colour_palette))
        self._generate_segments(start_index, middle - 1, segments)
        self._generate_segments(middle, end_index, segments)
