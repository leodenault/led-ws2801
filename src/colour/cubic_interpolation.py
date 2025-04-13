from colour.interpolation_mode import InterpolationMode


class CubicInterpolation(InterpolationMode):
    """Interpolates two colours using a cubic model.
    """

    def interpolate(self, colour1, colour2, colour1_weight):
        factor1 = colour1_weight * colour1_weight * colour1_weight
        factor2 = 1 - colour1_weight
        factor2 *= factor2 * factor2
        return colour1.multiply(factor1).add(colour2.multiply(factor2))
