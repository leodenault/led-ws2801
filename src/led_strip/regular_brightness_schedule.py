from datetime import datetime

from brightness_schedule import BrightnessSchedule


class RegularBrightnessSchedule(BrightnessSchedule):
    """Specifies a schedule for brightening and dimming the LEDs on a strip
    connected to a Raspberry Pi. Supports a regular schedule where the
    brightening and dimming happen at the same time every day.
    """

    def __init__(
      self,
      ramp_up_hour_start,
      ramp_up_hour_end,
      ramp_down_hour_start,
      ramp_down_hour_end,
      min_brightness,
      max_brightness):
        self.ramp_up_hour_start = ramp_up_hour_start
        self.ramp_up_hour_end = ramp_up_hour_end
        self.ramp_down_hour_start = ramp_down_hour_start
        self.ramp_down_hour_end = ramp_down_hour_end
        self.min_brightness = min_brightness
        self.max_brightness = max_brightness
        self.ramp_up_minute_start = ramp_up_hour_start * 60
        self.ramp_up_duration_minutes = (
                                          self.ramp_up_hour_end -
                                          ramp_up_hour_start) * 60
        self.ramp_down_minute_start = ramp_down_hour_start * 60
        self.ramp_down_duration_minutes = (
                                            ramp_down_hour_end -
                                            ramp_down_hour_start) * 60
        self.brightness_delta = max_brightness - min_brightness

    def get_brightness(self):
        current_time = datetime.now().time()
        current_hour = current_time.hour
        if (
          current_hour < self.ramp_up_hour_start or current_hour >=
          self.ramp_down_hour_end):
            return self.min_brightness
        if self.ramp_up_hour_end <= current_hour < self.ramp_down_hour_start:
            return self.max_brightness

        minute_of_day = current_hour * 60.0 + current_time.minute
        if current_hour < self.ramp_up_hour_end:
            completion = (
              (
                minute_of_day - self.ramp_up_minute_start) /
              self.ramp_up_duration_minutes)
            return completion * self.brightness_delta + self.min_brightness

        completion = (
          (
            minute_of_day - self.ramp_down_minute_start) /
          self.ramp_down_duration_minutes)
        return (1 - completion) * self.brightness_delta + self.min_brightness
