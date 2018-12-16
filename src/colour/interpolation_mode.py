from abc import ABCMeta, abstractmethod


class InterpolationMode:
    """Interpolates two colours together using a specific method.

    Subclasses should define the type of interpolation in their class name.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def interpolate(self, colour1, colour2, colour1_weight):
        """Returns a new colour created by interpolating between the two
        given colours.

        :param colour1: the first colour to use in interpolation.
        :param colour2: the second colour to use in interpolation.
        :param colour1_weight: the weight given to colour1 to use when
        interpolating between both colours. It is assumed that the weight of
        colour2 is 1 - colour1_weight.
        :return: a new colour which is the result of interpolating between
        colour1 and colour2.
        """
        pass
