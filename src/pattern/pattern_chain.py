from pattern import Pattern


class _AutocompletedPattern(Pattern):
    def __init__(self):
        pass

    def update(self, leds, delta):
        pass

    def is_done(self):
        return True


class PatternChain(Pattern):
    """A set of patterns which are chained together to form a sequence.
    """

    def __init__(self, completable_pattern_factories):
        self.pattern_factories = [factory for factory in
                                  completable_pattern_factories]
        self.current_pattern = _AutocompletedPattern()

    def update(self, leds, delta):
        if self.is_done():
            return

        if self.current_pattern.is_done():
            self.current_pattern = self.pattern_factories.pop(0)()

        self.current_pattern.update(leds, delta)

    def is_done(self):
        return (len(
          self.pattern_factories) == 0 and self.current_pattern.is_done())
