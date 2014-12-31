"""
Class to store information about a field in a card.
"""

class Field(object):
    """
    Class to store information about a field in a card.
    """
    
    def __init__(self, type, isList, public, required, initialVersion):
        """
        Constructor.
        
        :param type: Type of the object in the field (or type of a single value in the list in the field)
        :param isList: True if the field contains a list. False otherwise
        :param public: True if the field is a public one. False if it used internally
        :param required: True if the field is required in its class. False otherwise
        :param initialVersion: Initial version in which the card was allowed (tuple or list of length 3)
        """
        self.type           = type
        self.isList         = isList
        self.public         = public
        self.required       = required
        self.initialVersion = initialVersion
