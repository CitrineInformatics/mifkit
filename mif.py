"""
Definitions of classes and method used to build a Mif object.
"""

class Mif(object):
    """
    Class to store the high level objects in a Mif.
    """
    
    def __init__(self):
        """
        Default constructor. This takes no arguments; it just sets the default values.
        """
        self.entry = []
    
    def add_sample(self, sample):
        """
        Add a sample to the Mif.
        
        :param sample: Sample to add to the Mif.
        :type sample: Sample object
        """
        self.entry.append(sample)
