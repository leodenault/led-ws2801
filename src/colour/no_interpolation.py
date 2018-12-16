from interpolation_mode import InterpolationMode


class NoInterpolation(InterpolationMode):
    """Interpolation mode which does not interpolate between the two colours.

    If the weight of the first colour is greater than 0.5, then that colour is
    displayed. Otherwise, the second colour is displayed.
    """

    def interpolate(self, colour1, colour2, colour_1_weight):
        return colour1 if colour_1_weight > 0.5 else colour2


