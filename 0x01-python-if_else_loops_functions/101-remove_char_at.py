#!/usr/bin/python3
# 101-remove_char_at.py

def remove_char_at(s, n):
    """Create a copy of the string without the character at position n (C array index)."""
    if n < 0 or n >= len(s):
        return s
    result = ""
    for i in range(len(s)):
        if i != n:
            result += s[i]
    return result

# Test the function
original_string = "Hello, World!"
position_to_remove = 7
new_string = remove_char_at(original_string, position_to_remove)
print(new_string)
