import time

from sort_pattern import SortPattern, compare


class MergeSortPattern(SortPattern):
    """A pattern which randomly assigns colours to LEDs and sorts them using
    the merge sort algorithm.
    """

    def __init__(
      self,
      colour_distributor,
      sort_celebration,
      sort_step_duration):
        super(MergeSortPattern, self).__init__(
          colour_distributor,
          sort_celebration,
          sort_step_duration)

    def sort(self, leds, colour_palette, strip_data):
        self._recursive_merge_sort(
          leds,
          colour_palette,
          strip_data,
          0,
          leds.num_leds - 1)

    def _recursive_merge_sort(
      self,
      leds,
      colour_palette,
      strip_data,
      start_index,
      end_index):
        if start_index == end_index:
            return

        num_leds = end_index - start_index + 1
        middle = start_index + num_leds / 2
        self._recursive_merge_sort(
          leds,
          colour_palette,
          strip_data,
          start_index,
          middle - 1)
        self._recursive_merge_sort(
          leds,
          colour_palette,
          strip_data,
          middle,
          end_index)

        # Merge both sides together.
        while start_index <= end_index:
            if middle > end_index or start_index == middle:
                return
            if (not compare(
              strip_data[start_index],
              strip_data[middle],
              colour_palette)):
                next_colour = strip_data[middle]
                _shift_right(leds, strip_data, start_index, middle)
                strip_data[start_index] = next_colour
                leds.set_colour_and_display(
                  strip_data[start_index], start_index)
                time.sleep(self.sort_step_duration)
                middle += 1
            start_index += 1


def _shift_right(leds, strip_data, start_index, end_index):
    for i in range(end_index, start_index, -1):
        strip_data[i] = strip_data[i - 1]
        leds.set_colour(strip_data[i], i)
