"""
Class used to store information about a single sample.
"""

from mifkit.cards.card      import Card
from mifkit.cards.step      import Step
from mifkit.cards.reference import Reference
from mifkit.util.field      import Field
from mifkit.util.version    import Version

class Sample(Card):
    """
    Class to store a card with information about a sample.
    """
    
    _initialVersion = Version(1, 0, 0)
    
    _fields = Card._generateFields(             \
        record = Field(                         \
            type           = (Step),            \
            isList         = True,              \
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
