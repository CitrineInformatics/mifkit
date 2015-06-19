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
                 min         = None,
                 max         = None,
                 uncertainty = None):
        """
        Constructor

        :param value: Exact value for the point.
        :type value: Number or string with the value of the point.
        :param min: Minimum value for the point.
        :type min: Number or string with the minimum value of the point.
        :param max: Maximum value for the point.
        :type max: Number or string with the maximum value of the point.
        :param uncertainty: Isotropic uncertainty for the point.
        :type uncertainty: Number or string with the uncertainty of the point.
        """
        self.value       = value
        self.min         = min
        self.max         = max
        self.uncertainty = uncertainty
