"""
Definition of the base units of a general Mif object.
"""

class MifObject(object):
    """
    Base class for all Mif objects. All Mif objects contain an extra_field dictionary that stores fields that are
    not officially supported.
    """
    
    def __init__(self, extra_field = {}):
        """
        Constructor.
        
        :param extra_field: Dictionary of non-supported fields to save.
        :type extra_field: Dictionary with values that can be converted directly to Json (strings, numbers,
                           dictionaries, or lists of those types).
        """
        self.extra_field = extra_field
    
    def to_json_type(self):
        """
        Convert this object to a type that can be dumped as json.
        
        :returns: Object that can be serialized as json with the content of this object.
        """
        res = { self._to_camel_case(i): self.__dict__[i] for i in self.extra_field }
        res.update( { self._to_camel_case(i): self._convert_to_json_type(self.__dict__[i]) \
                for i in self.__dict__ if i is not self.extra_field } )
        return res
    
    def _convert_to_json_type(self, obj):
        """
        Convert obj to an object that is suitable for dumping as json. This function attempts to treat obj as
        a MifObject and otherwise returns obj.
        
        :returns: Input obj as an object that can be dumped as json.
        """
        try:
            return obj.to_json_type()
        except Exception:
            return obj
    
    def _to_camel_case(self, snake_case_string):
        """
        Convert a string from snake case to camel case.
        
        :param snake_case_string: Camel-cased string to convert to camel case.
        :returns: Camel-cased version of snake_case_string.
        """
        parts = snake_case_string.split('_')
        return parts[0] + ''.join([ i.title() for i in parts[1:] ])
