"""
Definitions of classes and method used to build a Mif object.
"""

import json
from objects.sample import Sample

class Mif(object):
    """
    Class to store the high level objects in a Mif and to write those values.
    """
    
    def __init__(self,         \
                 sample = None \
    ):
        """
        Constructor.
        
        :param sample: Samples to sample.
        :type sample: Sample object or list of Sample objects.
        """
        super(Mif, self).__init__()
        self.sample = sample
    
    def to_json_type(self):
        """
        Convert this object into one that can be dumped as json.
        
        :returns: Object or list that can be dumped as json.
        """
        res = self._get_samples()
        return res
    
    def _get_samples(self):
        """
        """
        return [ { 'sample': i.to_json_type() } for i in self.sample ] if isinstance(self.sample, list) else \
               [ { 'sample': self.sample.to_json_type() } ] if self.sample != None else                      \
               []
    
    def to_json(self, indent = None):
        """
        Convert this object into a JSON-encoded string.
        
        :param indent: Indent to apply to the json string.
        :returns: JSON-encoded string with the content of this object.
        """
        json_object = self.to_json_type()
        return json.dumps(json_object, ensure_ascii = False) if indent is None else \
               json.dumps(json_object, indent = indent, ensure_ascii = False)
