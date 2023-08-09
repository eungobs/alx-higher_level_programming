#!/usr/bin/python3
def uppercase(s):
    """Print a string in uppercase followed by a new line."""
    for char in s:
        diff = ord('a') - ord('A')
        print("{}".format(chr(ord(char) - diff)), end="")
    print("")  # Print a newline after processing the entire string

# Test the function
uppercase("Hello, World!")
