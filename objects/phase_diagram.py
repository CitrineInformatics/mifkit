from mif_object import MifObject
from line import Line
from phase import Phase
from point import Point
from person import Person
from reference import Reference


class PhaseDiagram(MifObject):
    """
    Class to store information about a phase diagram.

    The following fields must be defined:
        At least one of boundary, label, or phase
    """

    def __init__(self, vertex=None, boundary=None, label=None, phase=None, reference=None, contact=None,
                 license=None, data_type=None):
        """
        Constructor.

        :param vertex: Names of the vertices of the phase diagram (the order of these names should be consistent with
        the order of coordinates, e.g. in 2 dimensions, ["x", "y"] would place "x" at (1, 0) and "y" and (0, 2)).
        :type vertex: List of strings.

        :param boundary: List of lines that define boundaries within the phase diagram.
        :type boundary: Single Line object or list of Line objects.

        :param label: List of labels to add to the phase diagram (not including labels at vertices).
        :type label: Single Point object or list of Point objects.

        :param phase: List of phases that appear within the phase diagram. This is used when addition information about
        a phase is know besides a name or label.
        :type phase: Single Sample object or list of Sample objects.

        :param reference: References for the phase diagram.
        :type reference: Single Reference object or list of Reference objects.

        :param contact: List of people that worked on the phase diagram.
        :type contact: Single Person object or list of Person objects.

        :param license: One of more licenses to apply to the phase diagram.
        :type license: Single string or list of strings.

        :param data_type: Type of the data to add.
        :type data_type: String (either "Experimental" or "Computational")
        """
        self._boundary = None
        self._label = None
        self._phase = None
        self._reference = None
        self._contact = None
        self.vertex = vertex
        self.boundary = boundary
        self.label = label
        self.phase = phase
        self.reference = reference
        self.contact = contact
        self.license = license
        self.data_type = data_type

    @property
    def boundary(self):
        return self._boundary

    @boundary.setter
    def boundary(self, value):
        self._boundary = self._get_object(Line, value)

    @boundary.deleter
    def boundary(self):
        del self._boundary

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = self._get_object(Point, value)

    @label.deleter
    def label(self):
        del self._label

    @property
    def phase(self):
        return self._phase

    @phase.setter
    def phase(self, value):
        self._phase = self._get_object(Phase, value)

    @phase.deleter
    def phase(self):
        del self._phase

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, value):
        self._reference = self._get_object(Reference, value)

    @reference.deleter
    def reference(self):
        del self._reference

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        self._contact = self._get_object(Person, value)

    @contact.deleter
    def contact(self):
        del self._contact
