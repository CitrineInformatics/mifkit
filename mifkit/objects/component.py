from mif_object import MifObject


from mif_object import MifObject
from sample import Sample


class Component(MifObject):
    """
    Class to store information about a component of a system of materials.

    The following fields must be defined:
        label
        sample
    """

    def __init__(self, label=None, sample=None, **kwargs):
        """
        Constructor.

        :param label: Short description of the component. For example, "film" or "substrate".
        :type label: String.

        :param sample: Sample that makes up the component.
        :type common_name: Sample object.
        """
        super(Component, self).__init__(**kwargs)
        self._sample = None
        self.sample = sample
        self.label = label

    @property
    def sample(self):
        return self._sample

    @sample.setter
    def sample(self, value):
        self._sample = self._get_object(Sample, value)

    @sample.deleter
    def sample(self):
        del self._sample
