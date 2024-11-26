def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
  
    # list of numeric types
    numeric = [int, float, complex]
    
    # test to see whether x and y are int, float or complex. 
    # return -1 if either or both aren't numeric
    
    if type(x) in numeric and type(y) in numeric:
        print(y, x)
    else:
        return -1
    return


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

swap('Apple', 10)
swap(9, 17)
