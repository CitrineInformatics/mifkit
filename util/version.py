"""
Class to store information about the version of a card.
"""

class Version(object):
    """
    Class to store information about the version of a card.
    """
    
    def __init__(self, major = -1, minor = -1, revision = -1):
        """
        Constructor. Set the version to the defined values.
        
        :param major: Major version
        :param minor: Minor version
        :param revision: Revision version
        :raises: ValueError if any parameter is not an integer
        """
        try:
            self.set(major, minor, revision)
        except Exception:
            raise
    
    def set(self, major, minor, revision):
        """
        Set the major, minor, and revision versions.
        
        :param major: Major version
        :param minor: Minor version
        :param revision: Revision version
        :raises: ValueError if any parameter is not an integer
        """
        if isinstance(major, int) is False or isinstance(minor, int) is False or isinstance(revision, int) is False:
            raise ValueError('major, minor, and revision must be integers')
        self.major    = major
        self.minor    = minor
        self.revision = revision
    
    def compare(self, rhs):
        """
        Compare this Version to another.
        
        :param rhs: Version object to compare to
        :raises: ValueError if rhs is not a Version object
        :returns: Value greater than 0 if this object is greater than rhs
        :returns: Value equal to 0 if this object is the same as rhs
        :returns Value less than 0 if this object is less than rhs
        """
        if not isinstance(rhs, Version):
            raise ValueError('rhs must be a Version object')
        for i in ['major', 'minor', 'revision']:
            dif = getattr(self, i) - getattr(rhs, i)
            if dif != 0:
                return dif
        return 0
