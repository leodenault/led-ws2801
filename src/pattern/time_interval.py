class TimeInterval:
    """Measures a difference in time. Compatible with Pattern model.
    """

    def __init__(self, time_interval):
        """Instantiates a Timer.
        
        :param time_interval: the amount of time before this timer returns
        True when time_exceeded is called.
        """
        self.time_interval = time_interval
        self.elapsed_time = 0

    def time_exceeded(self, delta):
        """Returns whether the time interval measured by this TimeInterval
        has been exceeded.

        :param delta: the amount of time elapsed since the last call to this
        method.
        """
        self.elapsed_time += delta
        if self.elapsed_time > self.time_interval:
            self.elapsed_time = 0
            return True

        return False
