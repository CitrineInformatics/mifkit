from util.case import to_camel_case


class MifObject(object):
    """
    Base class for all MIF objects.
    """
    
    def __init__(self):
        """
        Constructor.
        """
        pass
    
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
        
        :returns: Input obj as an object that can be dumped as json.
        """
        if isinstance(obj, list):
            return [MifObject._convert_to_mif_dictionary(i) for i in obj]
        elif hasattr(obj, 'as_mif_dictionary'):
            return obj.as_mif_dictionary()
        else:
            return obj
