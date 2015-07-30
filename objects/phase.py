from mif_object import MifObject
from sample import Sample


class Phase(MifObject):
    """
    Class to store information about a phase on a phase diagram.

    The following fields must be defined:
        sample
        coordinate
    """

    def __init__(self, sample=None, coordinate=None):
        """
        Constructor.

        :param sample: Information about the sample at a point in the phase diagram.
        :type sample: Sample object.

        :param coordinate: Coordinate of the phase in the phase diagram.
        :type coordinate: List of numbers defining the coordinate.
        """
        self._sample = None
        self.sample = sample
        self.coordinate = coordinate

    @property
    def sample(self):
        return self._sample

    @sample.setter
    def sample(self, value):
        self._sample = self._get_object(Sample, value)

    @sample.deleter
    def sample(self):
        del self._sample
