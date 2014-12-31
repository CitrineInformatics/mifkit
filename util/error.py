"""
Class to store a MIF-related error.
"""

from mifkit.util.path import Path

class Error(object):
    """
    Class to store a MIF-related error.
    """
    
    def __init__(self, code = -1, path = [], details = []):
        """
        Constructor.
        
        :param code: Code to assign to the error
        :param path: List of Path object that define the path to the error
        :param details: List of details used when converting to the formatted error message
        """
        self.code    = code
        self.path    = path
        self.details = details if isinstance(details, (list, tuple)) else [ details ]
    
    def getMessage(self, variableName = 'VAR'):
        """
        Return the formatted version of this error.
        
        :param variableName: Name to assign to the encapsulating variable
        :returns: Formatted version of this error
        """
        res = 'Unknown error'
        try:
            res = self._codes[self.code]
            for i in range(len(self.details)):
                res = res.replace('#' + str(i+1), self.details[i])
        except Exception:
            pass
        return res + ' @ ' + variableName + ''.join([i.format() for i in self.path])
    
    def getSourceObject(self, start):
        """
        Return the object at which the error occured.
        
        :param start: Parent object from which the error was generated
        :raises: ValueError if the source object is not available from the error path
        :returns: Object where the error was generated
        """
        try:
            res = start
            for i in self.path:
                if i.isAttribute:
                    res = getattr(res, i.value)
                else:
                    res = res[i.value]
            return res
        except Exception:
            raise ValueError('Cannot access object')
    
    def getSourceObjectAndLastPath(self, start):
        """
        Return the object encapsulating the one at which the error occured.
        
        :param start: Parent object from which the error was generated
        :raises: ValueError if the source object is not available from the error path
        :returns: Object where the error was generated
        """
        try:
            res = start
            for i in range(len(self.path) - 1):
                if self.path[i].isAttribute:
                    res = getattr(res, self.path[i].value)
                else:
                    res = res[self.path[i].value]
            return res, self.path[-1]
        except Exception:
            raise ValueError('Cannot access object')
    
    @classmethod
    def compare(cls, obj1, obj2):
        """
        Compare two Error objects. Objects are compared is the following order.
        (1) sort by path, longest first
        (2) sort by code
        
        :param obj1: First object in the comparison
        :param obj2: Second object in the comparison
        :raises: ValueError if obj1 or obj2 is not an Error object
        :returns: Value less than 0 if obj1 < obj2
        :returns: Value greater than 0 if obj1 > obj2
        :returns: 0 if obj1 = obj2
        """
        if not isinstance(obj1, Error) or not isinstance(obj2, Error):
            raise ValueError('Unsupported class for object')
        pathDifference = len(obj2.path) - len(obj1.path)
        if pathDifference != 0:
            return pathDifference
        return obj1.code - obj2.code
        
    # List of errors that are supported. The order here is important since they will be fixed in this order
    _codes = {                               \
        1: 'Unsupported field (#1)',         \
        2: 'Missing required field (#1)',    \
        3: 'Unexpected type',                \
        4: 'Duplicate adhoc key (#1)',       \
        5: 'Object expected but found list', \
        6: 'List expected but found object'  \
    }
