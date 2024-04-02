#patel5a5
# Name:Akash Patel
# email:patel5a5@mai.uc.edu
# Assignment Number:06
# Due Date:02-22-2024
# Course/Section:IS4010
# Semester/Year:Spring/2024
# Brief Description of the assignment:We are using code from leetcode 
# Anything else that's relevant:



def patel5a5(x):
    # Convert the integer to a string
    x_str = str(x)
    
    # Check if the string is equal to its reverse
    return x_str == x_str[::-1]
def check_palindrome(x):
    if patel5a5(x):
        print(f"{x} is a palindrome.")
    else:
        print(f"{x} is not a palindrome.")
if __name__ == "__main__":
    # Example usage
    x = 121
    check_palindrome(x)  # Output: 121 is a palindrome
    
    # Test with other numbers
    check_palindrome(123)  # Output: 123 is not a palindrome
    check_palindrome(1221)  # Output: 1221 is a palindrome
    check_palindrome(12321)  # Output: 12321 is a palindrome