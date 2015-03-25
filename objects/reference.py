"""
Definitions for storing information about a reference.
"""

from mif_object import MifObject

class Reference(MifObject):
    """
    Class to store information about a reference.
    
    The following fields must be defined:
        None
    """
    
    def __init__(self,               \
                 doi         = None, \
                 isbn        = None, \
                 issn        = None, \
                 url         = None, \
                 publisher   = None, \
                 journal     = None, \
                 volume      = None, \
                 issue       = None, \
                 year        = None, \
                 pages       = None, \
                 author      = None, \
                 editor      = None, \
                 reference   = None  \
    ):
        """
        Constructor.
        
        :param doi: Doi of the reference.
        :type doi: String.
        :param isbn: ISBN of the reference.
        :type isbn: String or number.
        :param issn: ISSN of the reference.
        :type issn: String or number.
        :param url: URL of the reference.
        :type url: String.
        :param publisher: Publisher of the reference.
        :type publisher: String.
        :param journal: Journal in which the reference was published.
        :type journal: String.
        :param volume: Volume of the reference.
        :type volume: String or number.
        :param issue: Issue of the reference.
        :type issue: String or number.
        :param year: Year in which the reference was published.
        :type year: String or number.
        :param pages: Pages of the reference.
        :type pages: Pages object.
        :param author: List of authors of the reference.
        :type author: Single Name object or list of Name objects.
        :param editor: List of editors of the reference.
        :type editor: Single Name object or list of Name objects.
        :param reference: List of nested references.
        :type reference: Single Reference object or list of Reference objects.
        """
        super(Reference, self).__init__()
        self.doi         = doi
        self.isbn        = isbn
        self.issn        = issn
        self.url         = url
        self.publisher   = publisher
        self.journal     = journal
        self.volume      = volume
        self.issue       = issue
        self.year        = year
        self.pages       = pages
        self.author      = author
        self.editor      = editor
        self.reference   = reference
