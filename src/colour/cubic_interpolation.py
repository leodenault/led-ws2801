from interpolation_mode import InterpolationMode


class CubicInterpolation(InterpolationMode):
    """Interpolates two colours using a cubic model.
    """

    def interpolate(self, colour1, colour2, ratio):
        factor1 = ratio * ratio * ratio
        factor2 = 1 - ratio
        factor2 *= factor2 * factor2
        return colour1.multiply(factor1).add(colour2.multiply(factor2))
