from interpolation_mode import InterpolationMode


class LinearInterpolation(InterpolationMode):
    """Interpolates two colours using a linear model.
    """

    def interpolate(self, colour1, colour2, ratio):
        return colour1.multiply(ratio).add(colour2.multiply(1 - ratio))
