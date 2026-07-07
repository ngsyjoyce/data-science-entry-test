
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    

def swap(x, y):
    if (type(x) == int or type(x) == float) and (type(y) == int or type(y) == float): 
        x, y = y, x
        print(x, y)
    else:
        return -1


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10

if swap("Apple", 10) == -1:
    print(-1)

# - 9, 17
if swap(9, 17) == -1:
    print(-1)
