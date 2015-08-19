from mif_object import MifObject
from value import Value
from sample import Sample
from person import Person
from reference import Reference
from measurement import Measurement


class System(MifObject):
    """
    Class to store information about a system of materials.

    The following fields must be defined:
        sample
    """

    def __init__(self, sample=None, condition=None, measurement=None, reference=None, contact=None,
                 license=None, **kwargs):
        """
        Constructor.

        :param sample: List of samples in the system.
        :type sample: Single Sample object or list of Sample objects.

        :param condition: List of conditions of the system.
        :type condition: Single Value object or list of Value objects.

        :param measurement: List of measurements made on the system.
        :type measurement: Single Value object or list of Value objects.

        :param reference: List of references where information about the system is published.
        :type reference: Single Reference object or list of Reference objects.

        :param contact: List of people that worked on the system.
        :type contact: Single Person object or list of Person objects.

        :param license: One of more licenses to apply to the system.
        :type license: Single string or list of strings.
        """
        super(System, self).__init__(**kwargs)
        self._sample = None
        self._condition = None
        self._measurement = None
        self._reference = None
        self._contact = None
        self.sample = sample
        self.condition = condition
        self.measurement = measurement
        self.reference = reference
        self.contact = contact
        self.license = license

    @property
    def sample(self):
        return self._sample

    @sample.setter
    def sample(self, value):
        self._sample = self._get_object(Sample, value)

    @sample.deleter
    def sample(self):
        del self._sample

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
