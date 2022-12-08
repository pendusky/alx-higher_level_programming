#!/usr/bin/python3
def update_dictionary(my_dict, key, value):
    """
    Replacing or adding a key value if the key is there or not
    """
    if key in my_dict:
        my_dict.update({key: value})
    else:
        my_dict.update({key: value})
        return my_dict
