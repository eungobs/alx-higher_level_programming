def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                        'C': 100, 'D': 500, 'M': 1000}
    
    result = 0
    prev_value = 0
    
    for char in roman_string[::-1]:
        value = roman_dictionary[char]
        
        if value < prev_value:
            result -= value
        else:
            result += value
        
        prev_value = value
    
    return result

# Test cases
print(roman_to_int("X"))        # Output: 10
print(roman_to_int("VII"))      # Output: 7
print(roman_to_int("IX"))       # Output: 9
print(roman_to_int("LXXXVII"))  # Output: 87
print(roman_to_int("DCCVII"))   # Output: 707
