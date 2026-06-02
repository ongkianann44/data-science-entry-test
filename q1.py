def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    # Check if x and y are numeric
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return -1
    
    # Swap values
    
    x = x + y  # sum of both values
    y = x - y  # y is now value of x
    x = x - y  # x is now value of previous y

    print(f"Swapped values: x = {x}, y = {y}")

    # 4. Return the swapped values
    return x, y


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
