# function with the same name
# should solve to the leet code problem

def troegele(s: str) -> int:
    # Create a dictionary to map Roman symbols to their values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Initialize the result
    result = 0
    
    # Iterate through the Roman numeral string
    for i in range(len(s)):
        # If the current symbol is smaller than the next symbol, subtract its value
        if i < len(s) - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
            result -= roman_values[s[i]]
        else:
            result += roman_values[s[i]]
    
    return result

# Example usage
print(troegele("III"))  # Output: 3
print(troegele("LVIII"))  # Output: 58
print(troegele("MCMXCIV"))  # Output: 1994
