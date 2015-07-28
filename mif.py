import json
from util.case import to_snake_case


class Mif(object):
    """
    Class to store the high level objects in a MIF.
    """
    
    def __init__(self, objects=None):
        """
        Constructor.
        
        :param objects: Mif objects to save.
        :type objects: List of MifObject objects.
        """
        super(Mif, self).__init__()
        self.objects = objects

    def serialize(self, indent=None):
        """
        Convert this object into a JSON-encoded string.

        :param indent: Indent to apply to the json string.
        :type indent: Integer

        :returns: JSON-encoded string with the content of this object.
        """
        json_object = self._to_mif_array()
        return json.dumps(json_object, ensure_ascii=False) if indent is None else \
            json.dumps(json_object, indent=indent, ensure_ascii=False)

    def _to_mif_array(self):
        """
        Convert this object into one that can be dumped as json.

        :returns: Object or list that can be dumped as json.
        """
        res = self._get_mif_objects()
        return res[0] if len(res) == 1 else res
    
    def _get_mif_objects(self):
        """
        Get the list of objects stored by this object in a format ready for dumping to json.

        :returns: List of objects with proper MIF formatting applied.
        """
        objects = self.objects if isinstance(self.objects, list) else self.objects if self.objects is not None else []
        return [{to_snake_case(i.__name__): i.as_mif_dictionary()} for i in objects]
