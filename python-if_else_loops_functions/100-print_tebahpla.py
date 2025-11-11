#!/usr/bin/python3
def remove_char_at(str, n):
    """
    Creates a copy of the string, removing the character at position n.
    
    Args:
        str: The input string
        n: The position of the character to remove (0-based)
        
    Returns:
        A new string with the character at position n removed,
        or the original string if n is negative or out of bounds.
    """
    if n < 0 or n >= len(str):
        return str
    return str[:n] + str[n + 1:]
