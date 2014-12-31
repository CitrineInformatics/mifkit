"""
Class to store information about a process step.
"""

from mifkit.cards.card   import Card
from mifkit.util.field   import Field
from mifkit.util.version import Version

class Process(Card):
    """
    Class to store information about a process step.
    """
    
    _initialVersion = Version(1, 0, 0)
    
    _fields = Card._generateFields()
