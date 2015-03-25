"""
Definitions for storing information about a sample.
"""

from mif_object import MifObject

class Sample(MifObject):
    """
    Class to store information about a sample.
    
    
    The following fields must be defined:
        material
        measurement
    """
    
    def __init__(self,                \
                 material     = None, \
                 measurement  = None, \
                 reference    = None, \
                 experimenter = None  \
    ):
        """
        Constructor.
        
        :param material: Material that the sample is made from.
        :type material: Material object.
        :param measurement: List of measurements on the sample.
        :type measurement: Single Measurement object or list of Measurement objects.
        :param reference: List of references where information about the sample is published.
        :type reference: Single Reference object or list of Reference objects.
        :param experimenter: List of people that worked on the material.
        :type experimenter: Single Person object or list of Person objects.
        """
        super(Sample, self).__init__()
        self.material     = material
        self.measurement  = measurement
        self.reference    = reference
        self.experimenter = experimenter
