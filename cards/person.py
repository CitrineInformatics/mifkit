"""
Class to store information about a person.
"""

from mifkit.cards.card   import Card
from mifkit.util.field   import Field
from mifkit.util.version import Version

class Person(Card):
    """
    Class to store information about a person.
    """
    
    _initialVersion = Version(1, 0, 0)
    
    _fields = Card._generateFields(             \
        givenName = Field(                      \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        familyName = Field(                     \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        orcid = Field(                          \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0))  \
    )
