"""
Given a string, are all characters unique? True/False
"""


def is_unique_char(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True


print(is_unique_char("Peter"))
