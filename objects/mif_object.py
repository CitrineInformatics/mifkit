"""
Definition of the base units of a general Mif object.
"""

class MifObject(object):
    """
    Base class for all Mif objects.
    """
    
    def __init__(self):
        """
        Constructor.
        """
        pass
    
    def to_json_type(self):
        """
        Convert this object to a type that can be dumped as json.
        
        :returns: Object that can be serialized as json with the content of this object.
        """
        return { MifObject._to_camel_case(i): MifObject._convert_to_json_type(self.__dict__[i])
                 for i in self.__dict__ if self.__dict__[i] is not None }
    
    @staticmethod
    def _convert_to_json_type(obj):
        """
        Convert obj to an object that is suitable for dumping as json. This function attempts to treat obj as
        a MifObject and otherwise returns obj.
        
        :returns: Input obj as an object that can be dumped as json.
        """
        if isinstance(obj, list):
            return [ MifObject._convert_to_json_type(i) for i in obj ]
        else:
            try:
                return obj.to_json_type()
            except Exception:
                return obj
    
    @staticmethod
    def _to_camel_case(snake_case_string):
        """
        Convert a string from snake case to camel case.
        
        :param snake_case_string: Camel-cased string to convert to camel case.
        :returns: Camel-cased version of snake_case_string.
        """
        parts = snake_case_string.split('_')
        return parts[0] + ''.join([ i.title() for i in parts[1:] ])
