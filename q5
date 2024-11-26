def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    
    # list of numeric types
    numeric = [int, float]
    
    # check both num and divisor to see whether they're numeric 
    if type(num) not in numeric or type(divisor) not in numeric:
        print('Both num and divisor must be numeric')
        return -1
    
    # get the remainder using the modulo operator %
    # if divisor is 0, the ZeroDivisionError will be returned automatically
    
    remainder = num % divisor
        
    # if remainder is 0, return True. Otherwise, False is returned
    if remainder == 0:
        return True
    else:
        return False


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

is_div = check_divisibility(10, 2)
print(is_div)

is_div = check_divisibility(7, 3)
print(is_div)
