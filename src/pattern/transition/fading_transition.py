from transition import Transition
from display.led_strip import DrawingMode


class FadingTransition(Transition):
    """A transition that fades linearly from one pattern to the next.
    """

    def __init__(self, pattern1, pattern2, transition_time):
        super(FadingTransition, self).__init__(pattern1, pattern2)
        self.progress = 0
        self.transition_time = transition_time
        self.previous_transparency = None
        self.previous_drawing_mode = None

    def update_before_first_pattern(self, leds, delta):
        self.progress += delta / self.transition_time
        self.previous_transparency = leds.get_transparency()
        leds.set_transparency(1 - self.progress)

    def update_before_second_pattern(self, leds, delta):
        leds.set_transparency(self.progress)
        self.previous_drawing_mode = leds.get_drawing_mode()
        leds.set_drawing_mode(DrawingMode.BLEND)

    def update_after_second_pattern(self, leds, delta):
        leds.set_drawing_mode(self.previous_drawing_mode)
        leds.set_transparency(self.previous_transparency)

    def is_done(self):
        return self.progress >= 1
