import json
import collections


# Get the mapping from the file
# Returns None if error
def get_mapping(filename):
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

        mapping = collections.defaultdict(set)
        for out_map in mappings:
            inputs = out_map["inputkeys"]
            outputs = out_map["outputchannels"]
            for key in inputs:
                for out in outputs:
                    mapping[key].add(out)

        print(mapping)
        return mapping
    except json.JSONDecodeError as e:
        print(e)
        return None
