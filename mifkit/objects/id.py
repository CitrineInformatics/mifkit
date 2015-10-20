from mif_object import MifObject


class Id(MifObject):
    """
    Class to store information about an identifier.

    The following fields must be defined:
        name
        value
    """

    def __init__(self, name=None, value=None, **kwargs):
        """
        Constructor.

        :param name: Name of the identifier.
        :type name: String.

        :param value: Value of the identifier.
        :type value: String
        """
        super(Id, self).__init__(**kwargs)
        self.name = name
        self.value = value
