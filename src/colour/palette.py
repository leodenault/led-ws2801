"""Utility module for creating colour palettes.
"""
import random

_ALL_CANDIDATES = -1


def gradient(colour1, colour2, interpolation_mode, num_leds):
    """Creates a gradient between two colours.

    :param colour1: the colours used at the start of the gradient.
    :param colour2: the colour used at the end of the gradient.
    :param interpolation_mode: the InterpolationMode used to interpolate the
    colours.
    :param num_leds: the number of LEDs this gradient is expected to be
    displayed over.
    :return: a list of colours ordered in a gradient of colour1 to colour2.
    """
    return [
        interpolation_mode.interpolate(colour1, colour2, float(i) / num_leds)
        for i in range(0, num_leds)]


def choose_random_from(
  candidate_colours, min_colours=2, max_colours=_ALL_CANDIDATES):
    """Creates a colour palette by picking a random subset of colours from a
    candidate set.

    :param candidate_colours: the candidate set of colours from which to pick
    a subset.
    :param min_colours: the minimum number of colours the palette should
    contain.
    :param max_colours: the maximum number of colours the palette should
    contain.
    :return: a list of colours to be used as a palette. This list is made up
    of a subset of colours present in candidate_colours.
    """
    max_colours = (
        len(candidate_colours)
        if max_colours == _ALL_CANDIDATES else max_colours)
    num_colours = random.randint(min_colours, max_colours)
    temp_colours = [c for c in candidate_colours]
    palette = []

    while num_colours > 0:
        palette.append(
          temp_colours.pop(random.randint(0, len(temp_colours) - 1)))
        num_colours -= 1
    return palette
