"""
Base class for all card-type objects.
"""

import sys
import json
from mifkit.util.path    import Path
from mifkit.util.field   import Field
from mifkit.util.error   import Error
from mifkit.util.version import Version

class Card(object):
    """
    Base class for all card-type objects.
    """
    
    _initialVersion = Version(1, 0, 0)

    _fields = {                                 \
        'label': Field(                         \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        'adhoc': Field(                         \
            type           = (dict),            \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0))  \
    }
    
    def __init__(self, **kwargs):
        """
        Constructor. Sets the key/value pairs.
        """
        for key, value in kwargs.iteritems():
            self._saveKeyValuePair(key, value)
    
    @staticmethod
    def _generateFields(**kwargs):
        """
        Create a dictionary with the static member variables in this object combined with any key/value pairs passed
        in as arguments.
        
        :returns: New dictionary object the fields of this object combined with those in the arguments list
        """
        return dict(Card._fields, **kwargs)
    
    @classmethod
    def generate(cls, values):
        """
        Load values from a dictionary object.
        
        :param values: Dictionary object with the values to load
        """
        res = cls()
        for i in values:
            res._saveKeyValuePair(i, values[i])
        return res
    
    def getErrors(self, version = Version(sys.maxint, sys.maxint, sys.maxint)):
        """
        Look for errors in the card and its nested values.
        
        :param version: Tuple as (major, minor, revision) or string as 'major.minor.revision' or Version object
        :returns: List of errors with the card
        """
        version = self._getVersion(version)
        errors = self._validateCard(version)
        return self._formatErrors(errors)
    
    def correct(self, version = Version(sys.maxint, sys.maxint, sys.maxint), truncateLists = False):
        """
        Fix any errors in the card and its nested values.
        
        :param version: Tuple as (major, minor, revision) or string as 'major.minor.revision' or Version object
        :param truncateLists: True if when a list is found in place of an object, the first item should be saved from
                              the list, and the rest discarded. If false, and a list is encountered where an object
                              is expected, the error is ignored
        :returns: List of errors that could not be fixed
        """
        remainingErrors = []
        version = self._getVersion(version)
        errors = self._validateCard(version)
        for i in errors:
            remainingErrors += self._correctError(i, version, truncateLists, correctNestedErrors = True)
        return self._formatErrors(remainingErrors)
    
    def _saveKeyValuePair(self, key, value):
        """
        Save a key value pair in this object.
        
        :param key: Key of the value to save
        :param value: Value to save
        """
        try:
            field = self._fields[key]
            self._saveField(key, value, field)
        except Exception:
            setattr(self, key, value)
    
    def _saveField(self, key, value, field):
        """
        Save the value of a field in this object.
        
        :param key: Key of the value to save
        :param value: Value to save
        :param field: Field object with information about the field to save
        """
        if isinstance(value, list):
            self._saveList(key, value, field)
        else:
            self._saveItem(key, value, field)
    
    def _saveItem(self, key, value, field):
        """
        Save a single item in this object.
        
        :param key: Key of the value to save
        :param value: Value to save
        :param field: Field object with information about the field to save
        """
        if issubclass(field.type, Card):
            setattr(self, key, field.type.generate(value))
        else:
            setattr(self, key, value)
        
    def _saveList(self, key, value, field):
        """
        Save a list of items in this object as a list of items.
        
        :param key: Key of the values to save
        :param value: List of values to save
        :param field: Field object with information about the field to save
        """
        if issubclass(field.type, Card):
            setattr(self, key, [ field.type.generate(i) for i in value ])
        else:
            setattr(self, key, value)
    
    def _validateCard(self, version, path = []):
        """
        Check that all fields are valid in this object.
        
        :param version: Version object
        :param path: List of _Path objects defining the location of the card
        :returns: List of errors with the card
        """
        errors  = self._validateSetKeys(version, path)
        errors += self._validateRequiredFields(version, path)
        errors.sort(Error.compare)
        return errors
    
    def _validateSetKeys(self, version, path):
        """
        Check that all set fields are valid in this object.
        
        :param version: Version object
        :param path: List of _Path objects defining the location of the card
        :returns: List of errors with the card
        """
        errors = []
        for i in vars(self):
            if not self._validateKey(i, version, path):
                errors.append(Error(code = 1, path = path, details = i))
            else:
                errors += self._validateValue(version, path, i, self._fields[i], getattr(self, i))
        return errors
    
    def _validateKey(self, key, version, path):
        """
        Check that all fields are supported.
        
        :param key: Key to validate
        :param version: Version object
        :param path: List of _Path objects defining the location of the card
        :returns: True if key is valid
        :returns: False if key is not valid
        """
        if self._fields.has_key(key) is False:
            return False
        if self._fields[key].initialVersion.compare(version) > 0:
            return False
        return True
    
    def _validateValue(self, version, path, key, field, value):
        """
        Check that a value is of the correct type for a field.
        
        :param version: Version object
        :param path: List of _Path objects defining the location of the card
        :param key: Key of the field being checked
        :param field: Field object describing the value to check
        :param value: Value to check type of
        :returns: List of errors that were found
        """
        errors = []
        newPath = path + [ Path(key, True) ]
        if isinstance(value, list):
            if field.isList is False:
                errors.append(Error(code = 5, path = newPath, details = key))
            errors += self._validateList(version, newPath, key, field, value)
        else:
            if field.isList is True:
                errors.append(Error(code = 6, path = newPath, details = key))
            errors += self._validateItem(version, newPath, key, field, value)
        return errors
    
    def _validateList(self, version, path, key, field, value):
        """
        Check that each value in a list is of the correct type.
        
        :param version: Version object
        :param path: List of _Path objects defining the location of the card
        :param key: Key of the field being checked
        :param field: Field object describing the value to check
        :param value: Value to check type of
        :returns: List of errors that were found
        """
        errors = []
        for i in range(len(value)):
            errors += self._validateItem(version, path + [ Path(i, False) ], key, field, value[i])
        return errors
        
    def _validateItem(self, version, path, key, field, value):
        """
        Check that a single value is of the correct type.
        
        :param version: Version object
        :param path: List of _Path objects defining the location of the card
        :param key: Key of the field being checked
        :param field: Field object describing the value to check
        :param value: Value to check type of
        :returns: List of errors that were found
        """
        errors = []
        if isinstance(value, field.type) is False:
            errors.append(Error(code = 3, path = path, details = key))
        if hasattr(value, '_validateCard'):
            errors += value._validateCard(version, path)
        return errors
    
    def _validateRequiredFields(self, version, path):
        """
        Check that all required fields are present.
        
        :param version: Version object
        :param path: List of _Path objects defining the location of the card
        :returns: List of errors with the card
        """
        errors = []
        for i in self._fields:
            if self._fields[i].required is True and hasattr(self, i) is False:
                errors.append(Error(code = 2, path = path, details = i))
        return errors
    
    def _formatErrors(self, errors):
        """
        Format all errors that were found.
        
        :param errors: List of errors that were generated
        :returns: List of errors with the card
        """
        return [ i.getMessage(variableName = '<' + self.__class__.__name__ + '>') for i in errors ]
    
    def _correctError(self, error, version, truncateLists, correctNestedErrors):
        """
        Fix a single error.
        
        :param error: Error to fix
        :param version: Version object
        :param truncateLists: True to replace lists with objects where needed. False otherwise
        :param correctNestedErrors: True to look for and correct nested errors. False otherwise
        :returns: List of errors that could not be corrected
        """
        if error.code == 1:
            return self._correctUnsupportedField(error)
        elif error.code == 5:
            return self._correctListToObject(error, truncateLists)
        elif error.code == 6:
            return self._correctObjectToList(error)
        return [ error ]
    
    def _correctUnsupportedField(self, error):
        """
        Fix an unsupported field error.
        
        :param error: Error to fix
        :returns: List of errors that could not be corrected
        """
        key = error.details[0]
        card = error.getSourceObject(self)
        if not hasattr(card, 'adhoc'):
            card.adhoc = {}
        elif card.adhoc.has_key(key):
            return [ Error(code = 4, path = error.path + [ Path(adhoc, False) ], details = key) ]
        card.adhoc[key] = Card._convertToDictionaries(getattr(card, key))
        delattr(card, key)
        return []
    
    def _correctListToObject(self, error, truncateLists):
        """
        Fix an error where an object was expected but a list was found.
        
        :param error: Error to fix
        :param truncateLists: True to replace lists with objects where needed. False otherwise
        :returns: List of errors that could not be corrected
        """
        obj, path = error.getSourceObjectAndLastPath(self)
        if path.isAttribute:
            if self._correctListToObjectInAttribute(obj, path.value, truncateLists):
                return []
        else:
            if self._correctListToObjectInIndex(obj, path.value, truncateLists):
                return []
        return [ error ]
    
    def _correctListToObjectInAttribute(self, obj, path, truncateLists):
        """
        Fix an error where an object was expected but a list was found within an attribute
        
        :param obj: Object in which the attribute to fix exists
        :param path: Name of the attribute
        :param truncateLists: True to replace lists with objects where needed. False otherwise
        :returns: True if the error was corrected
        :returns: False if the error was not corrected
        """
        value = getattr(obj, path)
        if len(value) == 1 or truncateLists:
            setattr(obj, path, value[0])
            return True
        return False
    
    def _correctListToObjectInIndex(self, obj, path, truncateLists):
        """
        Fix an error where an object was expected but a list was found within an index (list or dict)
        
        :param obj: Object in which the index to fix exists
        :param path: Lookup of the list within the index
        :param truncateLists: True to replace lists with objects where needed. False otherwise
        :returns: True if the error was corrected
        :returns: False if the error was not corrected
        """
        value = obj[path]
        if len(value) == 1 or truncateLists:
            obj[path] = value[0]
            return True
        return False
    
    def _correctObjectToList(self, error):
        """
        Fix an error where a list was expected but an object was found.
        
        :param error: Error to fix
        :returns: List of errors that could not be corrected
        """
        obj, path = error.getSourceObjectAndLastPath(self)
        if path.isAttribute:
            setattr(obj, path.value, [ getattr(obj, path.value) ])
        else:
            obj[path.value] = [ obj[path.value] ]
        return []
    
    @classmethod
    def _convertToDictionaries(cls, value):
        """
        Recursively convert any object to a dictionary or list.
        
        :param value: Value to convert
        :returns: Input argument as a dictionary or list
        """
        if isinstance(value, Card):
            return cls._convertCardToDictionary(value)
        elif isinstance(value, list):
            return [ cls._convertToDictionaries(i) for i in value ]
        elif isinstance(value, dict):
            return { iKey : cls._convertToDictionaries(iValue) for iKey, iValue in value.iteritems() }
        else:
            return value
    
    @classmethod
    def _convertCardToDictionary(cls, value):
        """
        Recursively convert a card to a dictionary or list.
        
        :param value: Value to convert
        :returns: Input argument as a dictionary
        """
        res = { iKey : cls._convertToDictionaries(iValue) for iKey, iValue in vars(value).iteritems() }
    
    def _getVersion(self, version):
        """
        Get a version as a tuple of major, minor, and revision values as integers.
        
        :param version: Tuple as (major, minor, revision) or string as 'major.minor.revision' or Version object
        :raises: ValueError if version is not a tuple/list or a string
        :returns: Version object
        """
        if isinstance(version, Version):
            return version
        elif isinstance(version, (list, tuple)):
            return self._getVersionFromList(version)
        elif isinstance(version, (str, unicode)):
            return self._getVersionFromString(version)
        else:
            raise ValueError('Unknown type for version')
    
    def _getVersionFromList(self, version):
        """
        Get a version as a tuple of major, minor, and revision values as integers.
        
        :param version: Tuple as (major, minor, revision)
        :raises: ValueError if version does not contain a major, minor, and revision value
        :returns: Version object
        """
        if len(version) != 3:
            raise ValueError('Version must have length of exactly 3')
        return Version(int(version[0]), int(version[1]), int(version[2]))
    
    def _getVersionFromString(self, version):
        """
        Get a version as a tuple of major, minor, and revision values as integers.
        
        :param version: String as 'major.minor.revision'
        :raises: ValueError if version does not contain a major, minor, and revision value
        :returns: Version object
        """
        values = version.split('.')
        if len(values) != 3:
            raise ValueError('Version must have form \'major.minor.revision\'')
        return Version(int(values[0]), int(values[1]), int(values[2]))
