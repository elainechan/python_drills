"""
hamming.py

Finds the hamming distance between two DNA strands of identical length.
"""
def distance(strand1='', strand2=''):

    ham = 0

    for (x, y) in zip(strand1, strand2):
        if x != y:
            ham += 1
            
    return ham
