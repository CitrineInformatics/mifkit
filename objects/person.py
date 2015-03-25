"""
Definitions for storing information about a person.
"""

from mif_object import MifObject

class Person(MifObject):
    """
    Class to store information about a person.
    
    The following fields must be defined:
        At least one of name, email, or orcid
    """
    
    def __init__(self,               \
                 name        = None, \
                 email       = None, \
                 orcid       = None  \
    ):
        """
        Constructor.
        
        :param name: Name of the person.
        :type name: Name object.
        :param email: Email address of the person.
        :type email: String.
        :param orcid: ORCID identifier of the person.
        :type orcid: String.
        """
        super(Person, self).__init__()
        self.name  = name
        self.email = email
        self.orcid = orcid
