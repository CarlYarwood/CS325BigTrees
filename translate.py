'''
translate.py
Jon Beck

A program to read a DNA sense strand from a fasta file
and translate it into one-letter amino acid sequence.
Assumptions:
1. DNA is 5' to 3' and is a multiple of 3 in
length
2. fasta file has only one sequence
'''

#from readfasta import readfasta
from genetic_code import code

def get_codon(codon):
    return code[codon]


