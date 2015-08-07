from mif_object import MifObject


class Point(MifObject):
    """
    Class to store information about a point on a plot or phase diagram.

    The following fields must be defined:
        coordinate
    """

    def __init__(self, label=None, coordinate=None):
        """
        Constructor.

        :param label: Label to put on the point.
        :type label: String.

        :param coordinate: Coordinate of the point.
        :return: List of numbers defining the coordinate.
        """
        super(Point, self).__init__()
        self.label = label
        self.coodinate = coordinate
