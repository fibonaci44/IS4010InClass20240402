# create a function with the same name (6+2)
# Name: Matthew Lisowsky
# email: lisowsmd@mail.uc.edu
# Assignment Number: Assignment XX
# Due Date: 
# Course/Section: IS4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment:
# Citations:
# Anything else that's relevant:

def lisowsmd(nums, target):
    '''
    This leetcode runs two sum
    @parameter: none
    @return: two numbers
    '''
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # No valid pair found

if __name__ == "__main__":
    # Example usage
    nums = [2, 7, 11, 15]
    target = 9
    result = lisowsmd(nums, target)
    print("Indices of the two numbers:", result)  # Output: [0, 1]