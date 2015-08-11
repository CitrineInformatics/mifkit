from mif_object import MifObject
from scalar import Scalar


class Value(MifObject):
    """
    Class to store information about a single value.
    
    The following fields must be defined:
        name
        exactly one of scalar, vector, or matrix
    """
    
    def __init__(self, name=None, scalar=None, vector=None, matrix=None, units=None, **kwargs):
        """
        Constructor.
        
        :param name: Name of the value.
        :type name: String.

        :param scalar: Scalar value.
        :type scalar: Single/list of strings, numbers, or Scalar objects.

        :param vector: Vector value.
        :type vector: Single/list of lists of strings, numbers, or Scalar objects.

        :param matrix: Matrix value.
        :type matrix: Single/list of lists of lists of strings, numbers, or Scalar objects.

        :param units: Units of the value.
        :type units: String.
        """
        super(Value, self).__init__(**kwargs)
        self._scalar = None
        self._vector = None
        self._matrix = None
        self.name = name
        self.scalar = scalar
        self.vector = vector
        self.matrix = matrix
        self.units = units

    @property
    def scalar(self):
        return self._scalar

    @scalar.setter
    def scalar(self, value):
        self._scalar = self._get_object(Scalar, value)

    @scalar.deleter
    def scalar(self):
        del self._scalar

    @property
    def vector(self):
        return self._vector

    @vector.setter
    def vector(self, value):
        self._vector = self._get_object(Scalar, value)

    @vector.deleter
    def vector(self):
        del self._vector

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        self._matrix = self._get_object(Scalar, value)

    @matrix.deleter
    def matrix(self):
        del self._matrix
