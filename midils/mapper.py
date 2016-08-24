import json
import collections

'''Maps input keys to channel outputs based on a JSON config file
'''
class Mapper:
    def __init__(self, filename):
        """Creates a new mapper."""
        self._load_mapping(filename)

    def map(self, key):
        """Maps the input key to the outputs in the mapping. Returns None if not found"""
        if key not in self.mapping:
            return None
        return self.mapping[key]

    def _load_mapping(self, filename):
        """Load the mapping from the file. Sets mapping to None if error occurred.
        Output channels are 0-indexed"""
        try:
            config = json.loads(open(filename, 'r').read())
            key_begin = config["keybegin"]
            key_end = config["keyend"]
            output_begin = config["outputbegin"]
            output_end = config["outputend"]
            mappings = config["mappings"]
            # TODO validation

            # Inclusive
            num_keys = key_end - key_begin + 1
            num_outputs = output_end - output_begin + 1
            if num_keys < 0 or num_outputs < 0:
                print("Invalid number of keys or outputs")
                return None

            # The final mapping is a dictionary with key=input and value=set of outputs
            # Essentially takes the config's many-to-many and makes it a one-to-many
            mapping = collections.defaultdict(set)
            for out_map in mappings:
                inputs = out_map["inputkeys"]
                outputs = out_map["outputchannels"]
                for key in inputs:
                    if key_begin <= key <= key_end:
                        for out in outputs:
                            if output_begin <= out <= output_end:
                                mapping[key].add(out)
                            else:
                                print("Ignoring output {}: not in range".format(out))
                    else:
                        print("Ignoring input key {}: out of range".format(key))
            self.mapping = mapping
        except json.JSONDecodeError as e:
            print(e)
            self.mapping = {}
