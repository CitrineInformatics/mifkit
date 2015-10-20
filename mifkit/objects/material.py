from mif_object import MifObject
from id import Id
from composition import Composition
from value import Value


class Material(MifObject):
    """
    Class to store information about a material.
    
    The following fields must be defined:
        chemical_formula or common_name
    """
    
    def __init__(self, chemical_formula=None, common_name=None, composition=None, id=None, condition=None, **kwargs):
        """
        Constructor.
        
        :param chemical_formula: Chemical formula of the material.
        :type chemical_formula: String.

        :param common_name: Common name of the material.
        :type common_name: Single string or list of strings.

        :param composition: Composition of the material.
        :type composition: Single Composition object or list of Composition objects.

        :param id: One or more identifiers for the material.
        :type id: One or more Id objects.

        :param condition: Conditions of the material.
        :type condition: Single Value object or list of Value objects.
        """
        super(Material, self).__init__(**kwargs)
        self._composition = None
        self._id = None
        self._condition = None
        self.chemical_formula = chemical_formula
        self.common_name = common_name
        self.composition = composition
        self.id = id
        self.condition = condition

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
    def composition(self):
        return self._composition

    @composition.setter
    def composition(self, value):
        self._composition = self._get_object(Composition, value)

    @composition.deleter
    def composition(self):
        del self._composition

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = self._get_object(Id, value)

    @id.deleter
    def id(self):
        del self._id
