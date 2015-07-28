from mif_object import MifObject


class Pages(MifObject):
    """
    Class to store information about the pages of a reference.
    
    The following fields must be defined:
        start
    """
    
    def __init__(self, start=None, end=None):
        """
        Constructor.
        
        :param start: Starting page.
        :type start: String or number.

        :param end: Ending page.
        :type end: String or number.
        """
        super(Pages, self).__init__()
        self.start = start
        self.end = end
