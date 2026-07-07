def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """

    # Check if the num and divisor are numeric
    if (type(num) == int or type(num) == float) and (type(divisor) == int or type(divisor) == float):
        if num % divisor == 0:
            return True
        else:
            return False
    else:
        return -1
        
    

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:

# - 10, 2
print(check_divisibility(10, 2))

# - 7, 3
print(check_divisibility(7, 3))
