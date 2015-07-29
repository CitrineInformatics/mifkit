import json
import objects
from util.mif_encoder import MifEncoder
from util.case import keys_to_snake_case
from util.case import to_capitalized_camel_case


class Mif(object):
    """
    Class to store the high level objects in a MIF.
    """
    
    def __init__(self, object=None):
        """
        Constructor.
        
        :param object: Mif object(s) to save.
        :type object: Single MifObject object or list of MifObject objects.
        """
        super(Mif, self).__init__()
        self.object = object

    def dump(self, fp, **kwargs):
        """
        Convert this object into a JSON-encoded string and save it in a file.

        :param fp: Object to write the serialization to.
        :type fp: File-like object supporting .write() method.

        :param kwargs: Any options available to json.dump().
        """
        return json.dump(self.object, fp, cls=MifEncoder, **kwargs)

    def dumps(self, **kwargs):
        """
        Convert this object into a JSON-encoded string.

        :param kwargs: Any options available to json.dumps().

        :returns: JSON-encoded string with the content of this object.
        """
        return json.dumps(self.object, cls=MifEncoder, **kwargs)

    @staticmethod
    def load(fp, **kwargs):
        """
        Convert content in a JSON-encoded string to a Mif object.

        :param fp: Object to deserialize from.
        :type fp: File-like object supporting .read() method.

        :param kwargs: Any options available to json.load().

        :return: Mif object.
        """
        return Mif(object=Mif._to_mif_object(json.load(fp, **kwargs)))

    @staticmethod
    def loads(s, **kwargs):
        """
        Convert content in a JSON-encoded string to a Mif object.

        :param s: String to deserialize from.
        :type s: String.

        :param kwargs: Any options available to json.loads().

        :return: Mif object.
        """
        return Mif(object=Mif._to_mif_object(json.loads(s, **kwargs)))

    @staticmethod
    def _to_mif_object(obj):
        """
        Convert a dictionary or list of a single or multiple MifObject objects.

        :param obj: Object to convert.
        :type obj: Dictionary or list.

        :return: A single MifObject object or a list of MifObject objects.
        """
        if isinstance(obj, list):
            return [Mif._dict_to_mif_object(i) for i in obj]
        elif isinstance(obj, dict):
            return [Mif._dict_to_mif_object(obj)]
        else:
            raise ValueError('expecting list or dictionary as outermost structure')

    @staticmethod
    def _dict_to_mif_object(obj):
        """
        Convert a dictionary to a MifObject object based on its name.

        :param obj: Object to convert to a MifObject object.
        :type obj: Dictionary.

        :return: MifObject with the content of obj.
        """
        if len(obj) != 1:
            raise ValueError('Top-level mif object must contain exactly one key')
        key = obj.keys()[0]
        value = obj[key]
        if not isinstance(value, dict):
            raise ValueError(key + ' must have a value that is a dictionary')
        return getattr(objects, to_capitalized_camel_case(key))(**keys_to_snake_case(value))
