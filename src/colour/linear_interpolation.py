from interpolation_mode import InterpolationMode


class LinearInterpolation(InterpolationMode):
    """Interpolates two colours using a linear model.
    """

    def interpolate(self, colour1, colour2, colour1_weight):
        return colour1.multiply(colour1_weight).add(colour2.multiply(1 - colour1_weight))
