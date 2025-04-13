from abc import ABCMeta

from pattern.pattern import Pattern


class TimedPattern(Pattern):
    """A pattern that lasts a limited amount of time.
    """

    __metaclass__ = ABCMeta

    def __init__(self, display_time):
        """Instantiates a TimedPattern.

        :param display_time: the amount of time for which to display the
        pattern.
        """

        self.display_time = display_time
        self.elapsed_time = 0

    def update(self, leds, delta):
        self.elapsed_time += delta
        if self.is_done():
            return

    def is_done(self):
        return self.elapsed_time > self.display_time
