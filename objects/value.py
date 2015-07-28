from mif_object import MifObject


class Value(MifObject):
    """
    Class to store information about a single value.
    
    The following fields must be defined:
        name
        exactly one of scalar, vector, or matrix
    """
    
    def __init__(self, name=None, scalar=None, vector=None, matrix=None, units=None):
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
        super(Value, self).__init__()
        self.name = name
        self.scalar = scalar
        self.vector = vector
        self.matrix = matrix
        self.units = units
