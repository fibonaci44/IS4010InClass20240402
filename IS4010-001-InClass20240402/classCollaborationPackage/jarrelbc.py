# Name: Brianna Jarrell
# email: jarrelbc@mail.uc.edu
# Assignment Number: InClass_20240402
# Due Date: 4-2-24
# Course/Section:IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: Convert Roman numerals to integers
# Citations:
# Anything else that's relevant:

def jarrelbc(s: str) -> int:
    # Define the value for each Roman numeral
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    # Traverse the Roman numeral string from right to left
    for char in reversed(s):
        value = roman_values[char]
        
        # If the current value is less than the previous value, subtract it
        if value < prev_value:
            total -= value
        else:
            total += value
        
        # Update the previous value
        prev_value = value
    
    return total 


    