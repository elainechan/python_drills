"""
dna.py

Maps DNA nucleotides to RNA nucleotides.
"""

def to_rna(dna=''):

##    pairs = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
##    rna_values = [pairs[i] for i in dna]
##    rna_strand = ''.join(rna_values)
##    return rna_strand


    return ''.join([{'G':'C', 'C':'G', 'T':'A', 'A':'U'}[i] for i in dna])
