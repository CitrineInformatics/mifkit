"""
Definitions for a single scalar value / min / max / uncertainty.
"""

from mif_object import MifObject

class Scalar(MifObject):
    """
    Class to store information about a single scalar that contains a number or a string.

    The following fields must be defined:
        value and/or min and max
    """

    def __init__(self,
                 value       = None,
                 minimum     = None,
                 maximum     = None,
                 uncertainty = None):
        """
        Constructor

        :param value: Exact value for the point.
        :type value: Number or string with the value of the point.
        :param minimum: Minimum value for the point.
        :type minimum: Number or string with the minimum value of the point.
        :param maximum: Maximum value for the point.
        :type maximum: Number or string with the maximum value of the point.
        :param uncertainty: Isotropic uncertainty for the point.
        :type uncertainty: Number or string with the uncertainty of the point.
        """
        self.value       = value
        self.minimum     = minimum
        self.maximum     = maximum
        self.uncertainty = uncertainty
