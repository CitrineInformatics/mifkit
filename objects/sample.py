from mif_object import MifObject


class Sample(MifObject):
    """
    Class to store information about a sample.
    
    
    The following fields must be defined:
        material
        measurement
    """
    
    def __init__(self, material=None, measurement=None, reference=None, contact=None, license=None):
        """
        Constructor.
        
        :param material: Material that the sample is made from.
        :type material: Material object.

        :param measurement: List of measurements on the sample.
        :type measurement: Single Measurement object or list of Measurement objects.

        :param reference: List of references where information about the sample is published.
        :type reference: Single Reference object or list of Reference objects.

        :param contact: List of people that worked on the material.
        :type contact: Single Person object or list of Person objects.

        :param license: One of more licenses to apply to the sample.
        :type license: Single string or list of strings.
        """
        super(Sample, self).__init__()
        self.material = material
        self.measurement = measurement
        self.reference = reference
        self.contact = contact
        self.license = license
