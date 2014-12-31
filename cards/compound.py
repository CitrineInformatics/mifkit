"""
Class used to store information about a compound.
"""

from mifkit.cards.card     import Card
from mifkit.cards.property import Property
from mifkit.util.field     import Field
from mifkit.util.version   import Version

class Compound(Card):
    """
    Class to store a card with information about a compound.
    """

    _initialVersion = Version(1, 0, 0)

    _fields = Card._generateFields(             \
        name = Field(                           \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        chemicalFormula = Field(                \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        condition = Field(                      \
            type           = (Property),        \
            isList         = True,              \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0))  \
    )
