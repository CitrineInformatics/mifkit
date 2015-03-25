"""
Definitions for storing information about a sample.
"""

from mif_object import MifObject

class Sample(MifObject):
    """
    Class to store information about a sample.
    """
    
    def __init__(self, material = None, measurement = [], reference = [], experimenter = [], extra_field = {}):
        """
        Constructor.
        
        :param material: Material that the sample is made from.
        :type material: Material object.
        :param measurement: List of measurements on the sample.
        :type measurement: List of Measurement objects.
        :param reference: List of references where information about the sample is published.
        :type reference: List of Reference objects.
        :param experimenter: List of people that worked on the material.
        :type experimenter: List of Person objects.
        :param extra_field: Dictionary of non-supported fields to save.
        :type extra_field: Dictionary with values that can be converted directly to Json (strings, numbers,
                           dictionaries, or lists of those types).
        """
        super(Sample, self).__init__(extra_field)
        self.material     = material
        self.measurement  = measurement
        self.reference    = reference
        self.experimenter = experimenter
