"""
Class to store information about a step in a sample record.
"""

from mifkit.cards.card        import Card
from mifkit.cards.system      import System
from mifkit.cards.process     import Process
from mifkit.cards.measurement import Measurement
from mifkit.util.field        import Field
from mifkit.util.version      import Version

class Step(Card):
    """
    Class to store information about a step in a sample record.
    """
    
    _initialVersion = Version(1, 0, 0)
    
    _fields = Card._generateFields(             \
        system = Field(                         \
            type           = (System),          \
            isList         = True,              \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        process = Field(                        \
            type           = (Process),         \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        measurement = Field(                    \
            type           = (Measurement),     \
            isList         = True,              \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
    )
