def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Check both num and divisor are numeric
    if not isinstance(num, (int, float)):
        raise TypeError("The 'num' argument must be a numeric type (int or float).")
    if not isinstance(divisor, (int, float)):
        raise TypeError("The 'divisor' argument must be a numeric type (int or float).")

    # 2. Handle division by zero
    if divisor == 0:
        raise ValueError("Cannot check divisibility by zero.")

    else:
        result = num / divisor

    return float(result).is_integer()

#print(check_divisibility(10,2))
#print(check_divisibility(10,0))
print(check_divisibility(7,3))
