# shahh4.py
# Python function that calculates the square root of a non-negative integer x and returns the 
# result rounded down to the nearest integer using Bing AI
# Name: Harsh Shah
# email: shahh4@mail.uc.edu
# Assignment Number: InClass assignment
# Due Date: 04/02/2024
# Course/Section: IS4010-002
# Semester/Year: Spring 2024

def shahh4(x):
    # Base case: if x is 0 or 1, return x
    if x < 2:
        return x
    
    # Initialize left and right pointers for binary search
    left, right = 0, x
    
    # Binary search to find the square root
    while left < right:
        mid = left + (right - left) // 2
        if mid * mid <= x:
            left = mid + 1
        else:
            right = mid
    
    # Return the integer part of the square root
    return left - 1

if __name__ == "__main__":
    
    # Example test case
    x = 4
    print(f"Input: x = {x}")
    print(f"Output: {shahh4(x)}")
