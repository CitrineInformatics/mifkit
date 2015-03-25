"""
Definitions for storing information about a material.
"""

from mif_object import MifObject

class Material(MifObject):
    """
    Class to store information about a material.
    
    The following fields must be defined:
        chemical_formula
    """
    
    def __init__(self,                    \
                 chemical_formula = None, \
                 condition        = None  \
    ):
        """
        Constructor.
        
        :param chemical_formula: Chemical formula of the material.
        :type chemical_formula: String.
        :param condition: Conditions of the material.
        :type condition: Single Value object or list of Value objects.
        """
        super(Material, self).__init__()
        self.chemical_formula = chemical_formula
        self.condition        = condition
