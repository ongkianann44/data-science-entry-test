def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    # Validate that 's'
    if not isinstance(s, str):
        print("Error: input must be a string.")
        return s
    
    rev_str = ""
    for char in s:
        rev_str = char + rev_str
    

    return rev_str


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

#print(string_reverse("Hello World"))
#print(string_reverse(123))
print(string_reverse("Python"))
