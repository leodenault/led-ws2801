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
            return [strip_data[start_index]]
        else:
            num_leds = end_index - start_index + 1
            middle = start_index + num_leds / 2
            merged_left = self._recursive_merge_sort(
              leds,
              colour_palette,
              strip_data,
              start_index,
              middle - 1)
            merged_right = self._recursive_merge_sort(
              leds,
              colour_palette,
              strip_data,
              middle,
              end_index)

            # Merge both sides together.
            i = 0
            j = 0
            num_merged_left = len(merged_left)
            num_merged_right = len(merged_right)
            k = start_index
            while k <= end_index:
                if i == num_merged_left:
                    strip_data[k] = merged_right[j]
                    j += 1
                elif j == num_merged_right:
                    strip_data[k] = merged_left[i]
                    i += 1
                else:
                    from_left = compare(merged_left[i], merged_right[j],
                      colour_palette)
                    if from_left:
                        strip_data[k] = merged_left[i]
                        i += 1
                    else:
                        strip_data[k] = merged_right[j]
                        j += 1
                k += 1

            # Create temporary array with newly merged set and display the
            # colours to the strip.
            merged_all = []
            i = start_index
            while i <= end_index:
                merged_all.append(strip_data[i])
                if leds.get_colour_at(i) != strip_data[i]:
                    leds.set_colour_and_display(strip_data[i], i)
                    time.sleep(self.sort_step_duration)
                i += 1
            return merged_all
