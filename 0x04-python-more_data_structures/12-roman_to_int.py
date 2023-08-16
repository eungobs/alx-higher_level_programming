#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                        'C': 100, 'D': 500, 'M': 1000}
    result = 0
    item = 0
    roman = roman_string
    if type(roman) is not str or len(roman) == 0:
        return 0
    for item in range(item, len(roman)):
        if item < len(roman) - 1 and roman_dictionary[roman[item]] < roman_dictionary[roman[item + 1]]:
            result -= roman_dictionary[roman[item]]
        else:
            result += roman_dictionary[roman[item]]
    return result

# Test the roman_to_int function with different Roman numeral strings
roman_numeral = "X"
integer_value = roman_to_int(roman_numeral)
print(f"The integer value of {roman_numeral} is = {integer_value}")

roman_numeral = "VII"
integer_value = roman_to_int(roman_numeral)
print(f"The integer value of {roman_numeral} is = {integer_value}")

roman_numeral = "IX"
integer_value = roman_to_int(roman_numeral)
print(f"The integer value of {roman_numeral} is = {integer_value}")

roman_numeral = "LXXXVII"
integer_value = roman_to_int(roman_numeral)
print(f"The integer value of {roman_numeral} is = {integer_value}")

roman_numeral = "DCCVII"
integer_value = roman_to_int(roman_numeral)
print(f"The integer value of {roman_numeral} is = {integer_value}")
