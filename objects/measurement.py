"""
Definitions for storing measurements taken on a sample.
"""

from mif_object import MifObject

class Measurement(MifObject):
    """
    Class to store information about a measurement.
    
    
    The following fields must be defined:
        property
    """
    
    def __init__(self,                \
                 property     = None, \
                 data_type    = None, \
                 method       = None, \
                 condition    = None, \
                 reference    = None, \
                 experimenter = None  \
    ):
        """
        Constructor.
        
        :param property: Value of the property that was measured.
        :type property: Value object.
        :param data_type: Type of the data to add.
        :type data_type: String (either "Experimental" or "Computational")
        :param method: Description of the method of the measurement.
        :type method: String.
        :param condition: Conditions of the measurement.
        :type method: Single Value object or list of Value objects.
        :param reference: References in which information about the measurement is published.
        :type reference: Single Reference object or list of Reference objects.
        :param experimenter: List of people that worked on the measurement.
        :type experimenter: Single Person object or list of Person objects.
        """
        super(Measurement, self).__init__()
        self.property     = property
        self.data_type    = data_type
        self.method       = method
        self.condition    = condition
        self.reference    = reference
        self.experimenter = experimenter
