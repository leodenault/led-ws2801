from abc import ABCMeta, abstractmethod


class InterpolationMode:
    """Interpolates two colours together using a specific method.

    Subclasses should define the type of interpolation in their class name.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def interpolate(self, colour1, colour2, ratio):
        """Returns a new colour created by interpolating between the two
        given colours.

        :param colour1: the first colour to use in interpolation.
        :param colour2: the second colour to use in interpolation.
        :param ratio: the ratio of (colour1 / colour2) to use when
        interpolating between both colours.
        :return: a new colour which is the result of interpolating between
        colour1 and colour2.
        """
        pass
