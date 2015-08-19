from mifkit.util.case import to_camel_case
from mifkit.util.case import keys_to_snake_case


class MifObject(object):
    """
    Base class for all MIF objects.
    """
    
    def __init__(self, **kwargs):
        """
        Constructor.
        """
        for i in kwargs.keys():
            setattr(self, i, kwargs[i])
    
    def as_mif_dictionary(self):
        """
        Convert this object to a dictionary with formatting appropriate for a MIF.
        
        :returns: Dictionary with the content of this object formatted for a MIF.
        """
        return {to_camel_case(i): MifObject._convert_to_mif_dictionary(self.__dict__[i])
                for i in self.__dict__ if self.__dict__[i] is not None}

    @staticmethod
    def _convert_to_mif_dictionary(obj):
        """
        Convert obj to a dictionary with formatting appropriate for a MIF. This function attempts to treat obj as
        a MifObject and otherwise returns obj.

        :param obj: Object to convert to a dictionary.
        
        :returns: Input obj as an object that can be dumped as json.
        """
        if isinstance(obj, list):
            return [MifObject._convert_to_mif_dictionary(i) for i in obj]
        elif hasattr(obj, 'as_mif_dictionary'):
            return obj.as_mif_dictionary()
        else:
            return obj

    @staticmethod
    def _get_object(class_, obj):
        """
        Helper function that returns an object, or if it is a dictionary, initializes it from class_.

        :param class_: Class to use to instantiate object.

        :param obj: Object to process.

        :return: MifObject object or a list of MifObject objects.
        """
        if isinstance(obj, list):
            return [MifObject._get_object(class_, i) for i in obj]
        elif isinstance(obj, dict):
            return class_(**keys_to_snake_case(obj))
        else:
            return obj
