"""
Class used to store information about a single property.
"""

from mifkit.cards.card   import Card
from mifkit.util.field   import Field
from mifkit.util.version import Version

class Property(Card):
    """
    Class to store a card with information about a property.
    """
    
    _initialVersion = Version(1, 0, 0)

    _fields = Card._generateFields(             \
        name = Field(                           \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = True,              \
            initialVersion = Version(1, 0, 0)), \
        value = Field(                          \
            type           = (object),          \
            isList         = True,              \
            public         = True,              \
            required       = True,              \
            initialVersion = Version(1, 0, 0)), \
        certainty = Field(                      \
            type           = (object),          \
            isList         = True,              \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        units = Field(                          \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0))  \
    )
    