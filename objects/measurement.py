from mif_object import MifObject
from value import Value
from person import Person
from reference import Reference


class Measurement(MifObject):
    """
    Class to store information about a measurement.

    The following fields must be defined:
        property
    """
    
    def __init__(self, property=None, data_type=None, method=None, condition=None, reference=None, contact=None,
                 license=None):
        """
        Constructor.
        
        :param property: Value of the property that was measured.
        :type property: Value object.

        :param data_type: Type of the data to add.
        :type data_type: String (either "Experimental" or "Computational")

        :param method: Description of the method of the measurement.
        :type method: String.

        :param condition: Conditions of the measurement.
        :type condition: Single Value object or list of Value objects.

        :param reference: References in which information about the measurement is published.
        :type reference: Single Reference object or list of Reference objects.

        :param contact: List of people that worked on the measurement.
        :type contact: Single Person object or list of Person objects.

        :param license: One of more licenses to apply to the sample.
        :type license: Single string or list of strings.
        """
        super(Measurement, self).__init__()
        self._property = None
        self._condition = None
        self._reference = None
        self._contact = None
        self.property = property
        self.data_type = data_type
        self.method = method
        self.condition = condition
        self.reference = reference
        self.contact = contact
        self.license = license

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value):
        self._condition = self._get_object(Value, value)

    @condition.deleter
    def condition(self):
        del self._condition

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

    @property
    def property(self):
        return self._property

    @property.setter
    def property(self, value):
        self._property = self._get_object(Value, value)

    @property.deleter
    def property(self):
        del self._property

