#cunninig.PY

#number 205. Isomorphic Strings

def is_isomorphic() -> bool:
    """
    Determines if two predefined strings are isomorphic.

    Two strings are isomorphic if the characters in one can be replaced to get the other.
    All occurrences of a character must be replaced with another character while preserving the order of characters.
    No two characters may map to the same character, but a character may map to itself.

    Returns:
        bool: True if the predefined strings are isomorphic, False otherwise.
    """
    # Predefined strings for comparison
    s = "egg"
    t = "add"

    if len(s) != len(t):
        return False

    char_map = {}  # Dictionary to store character mappings
    used_chars = set()  # Set to track already mapped characters

    for i in range(len(s)):
        char_s, char_t = s[i], t[i]

        if char_s in char_map:
            if char_map[char_s] != char_t:
                return False
        else:
            if char_t in used_chars:
                return False
            char_map[char_s] = char_t
            used_chars.add(char_t)

    return True

if __name__ == "__main__":
    print(is_isomorphic())