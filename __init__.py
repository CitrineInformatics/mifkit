import json
from mifkit.cards.card        import Card
from mifkit.cards.citation    import Citation
from mifkit.cards.compound    import Compound
from mifkit.cards.measurement import Measurement
from mifkit.cards.person      import Person
from mifkit.cards.process     import Process
from mifkit.cards.property    import Property
from mifkit.cards.reference   import Reference
from mifkit.cards.sample      import Sample
from mifkit.cards.step        import Step
from mifkit.util.encoder      import Encoder

def load(fp):
    """
    Deserialize content of stream to a card object.
    
    :param fp: Object with a read() function to deserialize
    :returns: Object of 'Card' type with the deserialized content of the stream
    """
    return _loadJson(json.load(fp))

def loads(string):
    """
    Deserialize content of string to a card object.
    
    :param string: String to deserialize
    :returns: Object of 'Card' type with the deserialized content of the string
    """
    return _loadJson(json.loads(string))

def dump(obj, fp, **kwargs):
    """
    Serialize card to fp, an object complient with the json.dump fp parameter.
    
    :param obj: Object to serialize
    :param fp: Object to write serialization to
    """
    separators = (',', ':') if kwargs.get('indent', None) is None else (', ', ': ')
    json.dump(_getObject(obj), fp, cls = Encoder, separators = separators, **kwargs)

def dumps(obj, **kwargs):
    """
    Serialize card to a string.
    
    :param obj: Object to serialize
    :returns: String with the serialization of this object.
    """
    separators = (',', ':') if kwargs.get('indent', None) is None else (', ', ': ')
    return json.dumps(_getObject(obj), cls = Encoder, separators = separators, **kwargs)

def _getObject(obj):
    """
    Get the object to print when serializing a Card. This function returns a dictionary with the name of the class
    as the key.
    
    :param obj: Object being serialized
    :returns: Dictionary with the name of the card as the key
    """
    if isinstance(obj, list):
        if len(obj) is 1 and isinstance(obj[0], Card):
            return _cardToDict(obj[0])
        else:
            return [ _cardToDict(i) if isinstance(i, Card) else i for i in obj ]
    else:
        return _cardToDict(obj) if isinstance(obj, Card) else obj

def _cardToDict(obj):
    """
    Convert a Card object to a dictionary with the name of the Card class as the key.
    
    :param obj: Card to convert to a dictionary
    :returns: Dictionary with the card passed in as the only value
    """
    return dict([(obj.__class__.__name__, vars(obj))])

def _loadJson(obj):
    """
    Load data from an object.
    
    :param obj: Object with the information to convert
    :returns: List of objects that were extracted
    """
    if isinstance(obj, dict):
        return _objToCard(obj)
    if isinstance(obj, list):
        return [ _objToCard(i) for i in obj ]
    raise TypeError('Invalid json object in card deserialization')

def _objToCard(obj):
    """
    Load a card from an object.
    
    :param obj: Object to convert to a card
    :returns: Card with the data being deserialized
    """
    if isinstance(obj, dict) is False:
        raise TypeError('Invalid json object in card deserialization')
    return _dictToCard(obj)

def _dictToCard(obj):
    """
    Load a card from a dictionary.
    
    :param obj: Dictionary to convert to a card
    :returns: Card that was deserialized
    """
    type = _getCardType(obj)
    try:
        return globals()[type].generate(obj[type])
    except KeyError:
        return obj

def _getCardType(obj):
    """
    Get the type of a card being deserialized. Raises an exception in the case that the card type cannot be determined.
    
    :param obj: Object to get the card type of
    :returns: Type of the card
    """
    if len(obj) is not 1:
        raise TypeError('Card must contain exactly one value')
    return str(obj.iterkeys().next())
