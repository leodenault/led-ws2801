from pattern.pattern import Pattern
from abc import abstractmethod


def compare(colour1, colour2, colours):
    return colours.index(colour1) < colours.index(colour2)


class SortPattern(Pattern):
    """A pattern which randomly assigns colours to LEDs and sorts them.
    """

    def __init__(
      self,
      colour_distributor,
      sort_celebration,
      sort_step_duration):
        """Creates a SortPattern instance.

        :param colour_distributor: the ColourDistributor configuration used
        for randomly distributing colours at the beginning of the pattern
        animation.
        :param sort_celebration: the SortCelebration configuration for
        animating the end of the pattern.
        :param sort_step_duration: the amount of time between any operation
        in the sorting algorithm which modifies the location of a colour.
        """
        self.colour_distributor = colour_distributor
        self.sort_celebration = sort_celebration
        self.sort_step_duration = sort_step_duration

    def animate(self, leds, colour_palette):
        super(SortPattern, self).animate(leds, colour_palette)
        strip_data = self.colour_distributor.distribute(leds, colour_palette)
        self.sort(leds, colour_palette, strip_data)
        self.sort_celebration.celebrate(leds, strip_data)

    @abstractmethod
    def sort(self, leds, colour_palette, strip_data):
        """Sorts the colours on an LED strip

        :param leds: the LedStrip object used to communicate with the
        physical LED strip.
        :param colour_palette: the set of colours used as a reference for the
        ordering between colours.
        :param strip_data: the state of the set of colours which should be
        displayed to the LED strip.
        """
        pass
