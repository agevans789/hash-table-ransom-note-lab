def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    # 1. Create a frequency dictionary of all characters available in the magazine
    char_counts = {}
    for char in magazine:
        char_counts[char] = char_counts.get(char, 0) + 1
        
    # 2. Iterate through each character needed for the ransom note
    for char in ransomNote:
        # If the character is missing or no remaining counts are available, we cannot build it
        if char_counts.get(char, 0) <= 0:
            return False
        # Deduct the character from the available pool
        char_counts[char] -= 1
        
    # 3. If we successfully checked all characters, it is possible
    return True
