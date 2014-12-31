"""
Class used to store information about a reference.
"""

from mifkit.cards.card     import Card
from mifkit.cards.citation import Citation
from mifkit.util.field     import Field
from mifkit.util.version   import Version

class Reference(Card):
    """
    Class to store a card with information about a reference.
    """
    _initialVersion = Version(1, 0, 0)

Reference._fields = Card._generateFields(   \
    citation  = Field(                      \
        type           = (Citation),        \
        isList         = False,             \
        public         = True,              \
        required       = True,              \
        initialVersion = Version(1, 0, 0)), \
    reference = Field(                      \
        type           = (Reference),       \
        isList         = True,              \
        public         = True,              \
        required       = False,             \
        initialVersion = Version(1, 0, 0))  \
)
