def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    
    if type(lst) != list:
        print('%s is not a list' % lst)
        return -1
    
    # get number of items in the list
    list_length = len(lst)
    
    # initialize the index for list
    index = 0
    
    
    # look through the whole list and return the first negative number
    
    while index<list_length:
        if lst[index]<0:
            return lst[index]
        index += 1
        
    # if we've finished the while loop, then no negative numbers were found
    # return 'No negatives'
    return 'No negatives'


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

neg = find_first_negative([3, 5, -1, 7, -2, 8])
print(neg)

neg = find_first_negative([2, 10, 7, 0])
print(neg)
