"""
Definitions for storing information about a material.
"""

from mif_object import MifObject

class Material(MifObject):
    """
    Class to store information about a material.
    """
    
    def __init__(self, chemical_formula = None, condition = [], extra_field = {}):
        """
        Constructor.
        
        :param chemical_formula: Chemical formula of the material.
        :type chemical_formula: String.
        :param condition: List of conditions of the material.
        :type condition: List of Condition objects.
        :param extra_field: Dictionary of non-supported fields to save.
        :type extra_field: Dictionary with values that can be converted directly to Json (strings, numbers,
                           dictionaries, or lists of those types).
        """
        super(Material, self).__init__(extra_field)
        self.chemicalFormula = chemical_formula
        self.condition       = condition
