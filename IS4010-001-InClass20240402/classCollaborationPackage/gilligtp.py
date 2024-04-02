#gilligtp.py
def add_binary(a: str, b: str) -> str:
    # Initialize carry and result strings
    carry = 0
    result = []

    # Traverse both strings from right to left
    i, j = len(a) - 1, len(b) - 1
    while i >= 0 or j >= 0:
        # Get the current digits from a and b (or 0 if already exhausted)
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0

        # Calculate the sum of digits and carry
        total = digit_a + digit_b + carry
        carry, remainder = divmod(total, 2)

        # Append the remainder to the result
        result.append(str(remainder))

        # Move to the next position
        i -= 1
        j -= 1

    # If there's a remaining carry, add it to the result
    if carry:
        result.append(str(carry))

    # Reverse the result and join the digits
    return ''.join(result[::-1])

# Example usage
a = "11"
b = "1"
output = add_binary(a, b)
print(output)  # Output: "100"

if __name__ == "__main__":
    add_binary(a, b)