from brightness_schedule import BrightnessSchedule


class AlwaysMaxBrightnessSchedule(BrightnessSchedule):
    """A brightness schedule which always returns maximum brightness
    regardless of the time of day.
    """

    def __init__(self, max_brightness):
        self.max_brightness = max_brightness

    def get_brightness(self):
        return self.max_brightness
