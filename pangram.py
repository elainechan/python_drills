"""
pangram.py

Check if a string is a pangram.
"""


from string import ascii_lowercase
from collections import Counter


def is_pangram(sentence):
    """Return True if sentence is a pangram."""

    chars = set(sentence.lower())
    letters = set(ascii_lowercase).intersection(chars)
    return len(letters) >= 26
