def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    
    # get number of characters in s
    x = len(s)
    # initialize the new string
    new_s = ''
    
    # reverse all characters in s by using reversed range(x) and store in new_s
    for n in reversed(range(x)):
        new_s += s[n]
        
    # return the reversed string     
    return new_s


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

r = string_reverse('Hello World')
print(r)

r = string_reverse('Python')
print(r)
