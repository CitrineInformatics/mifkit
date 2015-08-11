from mif_object import MifObject
from name import Name


class Person(MifObject):
    """
    Class to store information about a person.
    
    The following fields must be defined:
        At least one of name, email, or orcid
    """
    
    def __init__(self, name=None, email=None, orcid=None, **kwargs):
        """
        Constructor.
        
        :param name: Name of the person.
        :type name: Name object.

        :param email: Email address of the person.
        :type email: String.

        :param orcid: ORCID identifier of the person.
        :type orcid: String.
        """
        super(Person, self).__init__(**kwargs)
        self._name = None
        self.name = name
        self.email = email
        self.orcid = orcid

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._get_object(Name, value)

    @name.deleter
    def name(self):
        del self._name
