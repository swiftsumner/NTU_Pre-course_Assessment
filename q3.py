def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    
    if type(dct) != dict:
        print('%s is not a dictionary' % dct)
        return -1
    
    # get original value from dct if it exists
    x = dct.get(key)
    
    # print the original value
    if x:
        print(x)
    
    # add/update value
    dct[key] = value
    
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

new_dct = update_dictionary({}, "name", "Alice")
print(new_dct)
new_dct = update_dictionary({"age": 25}, "age", 26)
print(new_dct)
