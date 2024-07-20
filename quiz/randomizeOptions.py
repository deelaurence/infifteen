import random

def randomly_switch_dict_items(d):
    keys = list(d.keys())
    # print(keys)
    # Example list of words

    # Extract words starting with 'b'
    options = [key for key in keys if key.startswith('option')]

    # print(d)

    if len(options) < 3:
        # print(d)
        # If dictionary has less than 3 items, cannot switch pairs
        return d
    
    
    
    
    # Choose two random keys
    key1, key2, key3, key4 = random.sample(options, 4)
    # print(key1,key2,key3,key4)
    # Swap their values
    d[key1], d[key2], d[key3], d[key4] = d[key2], d[key1], d[key4], d[key3]
    # print(d)
    return d
