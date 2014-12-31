import json
from mifkit.cards.card import Card

class Encoder(json.JSONEncoder):
    """
    Class to encode information in a card as a JSON object.
    """
    
    def default(self, obj):
        """
        Encode an object as a JSON object.
        
        :param obj: Object to encode
        :returns: JSON-encoded object
        """
        if isinstance(obj, Card):
            return vars(obj)
        else:
            return obj
