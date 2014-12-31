"""
Class used to store information about a measurement.
"""

from mifkit.cards.card   import Card
from mifkit.cards.person import Person
from mifkit.util.field   import Field
from mifkit.util.version import Version

class Citation(Card):
    """
    Class to store a card with information about a measurement.
    """
    
    _initialVersion = Version(1, 0, 0)
    
    _fields = Card._generateFields(             \
        type = Field(                           \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        doi = Field(                            \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        isbn = Field(                           \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        issn = Field(                           \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        url = Field(                            \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        author = Field(                         \
            type           = (Person),          \
            isList         = True,              \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        editor = Field(                         \
            type           = (Person),          \
            isList         = True,              \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        publisher = Field(                      \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        title = Field(                          \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        edition = Field(                        \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        journal = Field(                        \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        volume = Field(                         \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        issue = Field(                          \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        year = Field(                           \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        pageStart = Field(                      \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0)), \
        pageEnd = Field(                        \
            type           = (str, unicode),    \
            isList         = False,             \
            public         = True,              \
            required       = False,             \
            initialVersion = Version(1, 0, 0))  \
    )
