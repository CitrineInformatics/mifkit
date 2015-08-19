from mif_object import MifObject
from system import System
from person import Person
from reference import Reference
from measurement import Measurement


class Reaction(MifObject):
    """
    Class to store information about a reaction.

    The following fields must be defined:
        reactant
        product
    """

    def __init__(self, reactant=None, product=None, catalyst=None, measurement=None, reference=None, contact=None,
                 license=None, **kwargs):
        """
        Constructor.

        :param reactant: List of reactants in the reaction.
        :type reactant: Single Sample/System object or list of Sample/System objects.

        :param product: List of products of the reaction.
        :type product: Single Sample/System object or list of Sample/System objects.

        :param catalyst: List of catalysts of the reaction.
        :type catalyst: Single Sample/System object or list of Sample/System objects.

        :param measurement: List of measurements made on the reaction.
        :type measurement: Single Value object or list of Value objects.

        :param reference: List of references where information about the reaction is published.
        :type reference: Single Reference object or list of Reference objects.

        :param contact: List of people that worked on the reaction.
        :type contact: Single Person object or list of Person objects.

        :param license: One of more licenses to apply to the reaction.
        :type license: Single string or list of strings.
        """
        super(Reaction, self).__init__(**kwargs)
        self._reactant = None
        self._product = None
        self._catalyst = None
        self._measurement = None
        self._reference = None
        self._contact = None
        self.reactant = reactant
        self.product = product
        self.catalyst = catalyst
        self.measurement = measurement
        self.reference = reference
        self.contact = contact
        self.license = license

    @property
    def reactant(self):
        return self._reactant

    @reactant.setter
    def reactant(self, value):
        self._reactant = self._get_object(System, value)

    @reactant.deleter
    def reactant(self):
        del self._reactant

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = self._get_object(System, value)

    @product.deleter
    def product(self):
        del self._product

    @property
    def catalyst(self):
        return self._catalyst

    @catalyst.setter
    def catalyst(self, value):
        self._catalyst = self._get_object(System, value)

    @catalyst.deleter
    def catalyst(self):
        del self._catalyst

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
