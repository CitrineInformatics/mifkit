import json
from util.case import to_snake_case


class MifEncoder(json.JSONEncoder):
    """
    Class to convert MifObject objects to json.
    """

    def default(self, obj):
        """
        Convert an object to a form ready to dump to json.

        :param obj: Object being serialized.

        :return: List or dictionary.
        """
        res = self._get_mif_objects(obj)
        return res[0] if len(res) == 1 else res

    @staticmethod
    def _get_mif_objects(obj):
        """
        Get the list of objects stored by this object in a format ready for dumping to json.

        :param obj: Object being serialized.

        :returns: List of objects with proper MIF formatting applied.
        """
        mod_object = [] if obj is None else obj if isinstance(obj, list) else [obj]
        return [{to_snake_case(i.__class__.__name__): i.as_mif_dictionary()} for i in mod_object]
