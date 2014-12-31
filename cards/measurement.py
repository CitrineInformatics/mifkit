"""
Class used to store information about a measurement.
"""

from mifkit.cards.card     import Card
from mifkit.cards.property import Property
from mifkit.util.field     import Field
from mifkit.util.version   import Version

class Measurement(Card):
    """
    Class to store a card with information about a measurement.
    """
    
    _initialVersion = Version(1, 0, 0)

    _fields = Card._generateFields(             \
        value = Field(                          \
            type           = (Property),        \
            isList         = False,             \
            public         = True,              \
            required       = True,              \
            initialVersion = Version(1, 0, 0)), \
        condition = Field(                      \
            type           = (Property),        \
            isList         = True,              \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        dataType = Field(                       \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        method = Field()
    )
