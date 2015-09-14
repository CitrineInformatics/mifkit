from mif_object import MifObject


class Composition(MifObject):
    """
    Class to store information about the composition of a material.

    The following fields must be defined:
        element
        weight_percent or atomic_percent
    """

    def __init__(self, element=None, weight_percent=None, atomic_percent=None, **kwargs):
        """
        Constructor.

        :param element: Symbol of the element.
        :type element: String.

        :param weight_percent: Percentage of weight of the material that is this element.
        :type weight_percent: String or number.

        :param atomic_percent: Percentage of the atoms in the material this is this element.
        :type atomic_percent: String or number.
        """
        super(Composition, self).__init__(**kwargs)
        self.element = element
        self.weight_percent = weight_percent
        self.atomic_percent = atomic_percent
