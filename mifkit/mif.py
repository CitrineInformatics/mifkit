import json
import objects
from mifkit.util.mif_encoder import MifEncoder
from mifkit.util.case import keys_to_snake_case
from mifkit.util.case import to_capitalized_camel_case


def dump(mif_object, fp, **kwargs):
    """
    Convert this object into a JSON-encoded string and save it in a file.

    :param mif_object: Object to serialize.
    :type mif_object: Single MifObject-type object or list of MifObject-type objects.

    :param fp: Object to write the serialization to.
    :type fp: File-like object supporting .write() method.

    :param kwargs: Any options available to json.dump().
    """
    json.dump(mif_object, fp, cls=MifEncoder, **kwargs)


def dumps(mif_object, **kwargs):
    """
    Convert this object into a JSON-encoded string.

    :param mif_object: Object to serialize.
    :type mif_object: Single MifObject-type object or list of MifObject-type objects.

    :param kwargs: Any options available to json.dumps().
    """
    json.dumps(mif_object, cls=MifEncoder, **kwargs)


def load(fp, **kwargs):
    """
    Convert content in a JSON-encoded string to a Mif object.

    :param fp: Object to deserialize from.
    :type fp: File-like object supporting .read() method.

    :param kwargs: Any options available to json.load().

    :return: Single MifObject-type object or list of MifObject-type objects.
    """
    return _to_mif_object(json.load(fp, **kwargs))


def loads(s, **kwargs):
    """
    Convert content in a JSON-encoded string to a Mif object.

    :param s: String to deserialize from.
    :type s: String.

    :param kwargs: Any options available to json.loads().

    :return: Single MifObject-type object or list of MifObject-type objects.
    """
    return _to_mif_object(json.loads(s, **kwargs))


def from_dict(obj):
    """
    Convert content in a list or dictionary to

    :param obj: Python object to convert to MifObject type.
    :type obj: List or dictionary.

    :return: Single MifObject-type object or list of MifObject-type objects.
    """
    return _to_mif_object(obj)


def _to_mif_object(obj):
    """
    Convert a dictionary or list of a single or multiple MifObject objects.

    :param obj: Object to convert.
    :type obj: Dictionary or list.

    :return: A single MifObject object or a list of MifObject objects.
    """
    if isinstance(obj, list):
        return [_dict_to_mif_object(i) for i in obj]
    elif isinstance(obj, dict):
        return [_dict_to_mif_object(obj)]
    else:
        raise ValueError('expecting list or dictionary as outermost structure')


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


class Mif(object):
    """
    Legacy class. Don't use this. It's only here to prevent old scripts from breaking.
    """

    def __init__(self, sample=None):
        """
        Constructor.

        :param sample: Samples to sample.
        :type sample: Sample object or list of Sample objects.
        """
        super(Mif, self).__init__()
        self.sample = sample

    def to_json(self, indent=None):
        """
        Convert this object into a JSON-encoded string.

        :param indent: Indent to apply to the json string.
        :returns: JSON-encoded string with the content of this object.
        """
        return json.dumps(self.sample) if indent is None else json.dumps(self.sample, indent=indent)
