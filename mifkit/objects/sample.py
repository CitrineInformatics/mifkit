from mif_object import MifObject
from person import Person
from material import Material
from reference import Reference
from measurement import Measurement


class Sample(MifObject):
    """
    Class to store information about a sample.

    The following fields must be defined:
        material
    """
    
    def __init__(self, material=None, measurement=None, reference=None, contact=None, license=None, **kwargs):
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
        super(Sample, self).__init__(**kwargs)
        self._material = None
        self._measurement = None
        self._reference = None
        self._contact = None
        self.material = material
        self.measurement = measurement
        self.reference = reference
        self.contact = contact
        self.license = license

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        self._material = self._get_object(Material, value)

    @material.deleter
    def material(self):
        del self._material

    @property
    def measurement(self):
        return self._measurement

    @measurement.setter
    def measurement(self, value):
        self._measurement = self._get_object(Measurement, value)

    @measurement.deleter
    def measurement(self):
        del self._measurement

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, value):
        self._reference = self._get_object(Reference, value)

    @reference.deleter
    def reference(self):
        del self._reference

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        self._contact = self._get_object(Person, value)

    @contact.deleter
    def contact(self):
        del self._contact
