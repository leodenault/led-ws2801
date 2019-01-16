from colour import led_colour
from pattern.pattern_chain import PatternChain
from pattern.sorting.bubble_sort_pattern import BubbleSortPattern
from pattern.sorting.colour_distributor import ColourDistributor
from pattern.sorting.merge_sort_pattern import MergeSortPattern
from pattern.sorting.sort_celebration import SortCelebration


def compare(colour1, colour2, colours):
    return colours.index(colour1) < colours.index(colour2)


def create_bubble_sort_pattern(
  num_leds,
  distribution_duration,
  sort_step_duration,
  num_celebration_flashes,
  celebration_flash_duration,
  colour_palette):
    """Creates a pattern instance that sorts colours using the bubble sort
    algorithm.

    :param num_leds: the number of LEDs on the device.
    :param distribution_duration: the time it should take to distribute all
    colours across the LED strip.
    :param sort_step_duration: the amount of time a single step takes to
    execute.
    :param num_celebration_flashes: the number of times the LEDs should flash
    in celebration.
    :param celebration_flash_duration: the amount of time, in seconds,
    it should take for a single flash to occur.
    :param colour_palette: the palette of colours which will be used to
    randomly distribute colours onto the strip.
    """
    strip_data = [led_colour.BLACK] * num_leds
    return PatternChain([
        lambda:
        ColourDistributor(
          num_leds, distribution_duration, colour_palette, strip_data),
        lambda:
        BubbleSortPattern(colour_palette, strip_data, sort_step_duration),
        lambda:
        SortCelebration(
          num_celebration_flashes, celebration_flash_duration, strip_data),
    ])


def create_merge_sort_pattern(
  num_leds,
  distribution_duration,
  sort_step_duration,
  num_celebration_flashes,
  celebration_flash_duration,
  colour_palette):
    """Creates a pattern instance that sorts colours using the merge sort
    algorithm.

    :param num_leds: the number of LEDs on the device.
    :param distribution_duration: the time it should take to distribute all
    colours across the LED strip.
    :param sort_step_duration: the amount of time a single step takes to
    execute.
    :param num_celebration_flashes: the number of times the LEDs should flash
    in celebration.
    :param celebration_flash_duration: the amount of time, in seconds,
    it should take for a single flash to occur.
    :param colour_palette: the palette of colours which will be used to
    randomly distribute colours onto the strip.
    """
    strip_data = [led_colour.BLACK] * num_leds
    return PatternChain([
        lambda:
        ColourDistributor(
          num_leds, distribution_duration, colour_palette, strip_data),
        lambda:
        MergeSortPattern(num_leds, sort_step_duration, colour_palette, strip_data),
        lambda:
        SortCelebration(
          num_celebration_flashes, celebration_flash_duration, strip_data),

    ])
