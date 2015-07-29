from mif_object import MifObject
from name import Name
from pages import Pages


class Reference(MifObject):
    """
    Class to store information about a reference.
    
    The following fields must be defined:
        None
    """
    
    def __init__(self, doi=None, isbn=None, issn=None, url=None, title=None, publisher=None, journal=None, volume=None,
                 issue=None, year=None, pages=None, author=None, editor=None, reference=None):
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
        
        :param title: Title of the reference.
        :type title: String.

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
        self._pages = None
        self._author = None
        self._editor = None
        self._reference = None
        self.doi = doi
        self.isbn = isbn
        self.issn = issn
        self.url = url
        self.title = title
        self.publisher = publisher
        self.journal = journal
        self.volume = volume
        self.issue = issue
        self.year = year
        self.pages = pages
        self.author = author
        self.editor = editor
        self.reference = reference

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        self._pages = self._get_object(Pages, value)

    @pages.deleter
    def pages(self):
        del self._pages

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = self._get_object(Name, value)

    @author.deleter
    def author(self):
        del self._author

    @property
    def editor(self):
        return self._editor

    @editor.setter
    def editor(self, value):
        self._editor = self._get_object(Name, value)

    @editor.deleter
    def editor(self):
        del self._editor

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, value):
        self._reference = self._get_object(Reference, value)

    @reference.deleter
    def reference(self):
        del self._reference
