from mif_object import MifObject


class Name(MifObject):
    """
    Class to store information about the name of a person.
    
    The following fields must be defined:
        family
    """
    
    def __init__(self, given=None, family=None, **kwargs):
        """
        Constructor.
        
        :param given: Given name.
        :type given: String.

        :param family: Family name.
        :type family: String.
        """
        super(Name, self).__init__(**kwargs)
        self.given = given
        self.family = family
