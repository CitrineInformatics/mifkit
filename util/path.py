"""
Class for storing the path to an element of a MIF.
"""

class Path(object):
    """
    Class to store information about the path to a variable nested in a card.
    """
    
    def __init__(self, value, isAttribute):
        """
        Constructor.
        
        :param value: Value of the path
        :param isAttribute: True if value is an attribute of class. False otherwise.
        """
        self.value       = value
        self.isAttribute = isAttribute
    
    def format(self):
        """
        Format this object for printing.
        
        :returns: Formatted version of this object
        """
        if self.isAttribute:
            return '.' + self.value
        else:
            return '[' + str(self.value) + ']'
