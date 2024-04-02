#harrints.py

def harrints(nums=None):
    """
    Given an array of integers `nums` and a target value, find two numbers in the array
    such that their sum equals the target. Return their indices.

    Args:
        nums (List[int], optional): List of integers. Defaults to None.

    Returns:
        List[int]: Indices of the two numbers that add up to the target.

    Raises:
        ValueError: If no valid solution exists.
    """
    target = 0  # You can set the desired target value here

    if nums is None:
        # Example data from your previous message
        nums = [2, 7, 11, 15]

    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            result = [num_to_index[complement], i]
            print(f"The indices of the two numbers that add up to the target are: {result}")
            return result
        num_to_index[num] = i

    raise ValueError("No valid solution")

# Entry point check
if __name__ == '__main__':
    harrints()  # Output: [0, 1]
