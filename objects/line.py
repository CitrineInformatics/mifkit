from mif_object import MifObject


class Line(MifObject):
    """
    Class to store information about a line on a plot or phase diagram.

    The following fields must be defined:
        coordinate
    """

    def __init__(self, label=None, coordinate=None):
        """
        Constructor.

        :param label: Label to put on the line.
        :type label: String.

        :param coordinate: Coordinates of points on the line (in the order they should be connected).
        :type coordinate: List of lists of numbers, with each sub-list representing a coordinate.
        """
        self.label = label
        self.coordinate = coordinate
