def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    
    # return an error message if lst is not a list
    
    if type(lst)!=list:
        print('A list must be provided. %s is not a list.' % str(lst))
        return -1
    
    # initialize the index counter for lst
    x = 0
    
    # compare find_val against every item in lst and replace with replace_val if found
    for l in lst:
        if find_val==l:
            lst[x] = replace_val
        # increment the counter
        x += 1
    
    return lst


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

new_list = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print(new_list)

new_list = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print(new_list)
