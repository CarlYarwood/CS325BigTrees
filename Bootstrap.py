'''
This file is responsible for running bootstrapping methods with our 
UPGMA tree building algorithm

Eli Charleville
Nov 12 2018


1. Align all sequences
2. choose random columns, 
    - create new set of sequences
3. Build a new tree with these sequences 
4. repeat until satisfied
5. take statistics on clades to get confidence values 
'''

import random

'''
get_bootstrap_list - takes in an array of sequences that have already been aligned
and samples accordingly until we have a new set of sequences the same 
length as the original

Param -- fasta_list: must be an array strings 



Returns: a new set of sequences randomly selected

'''

def get_bootstrap_list(fasta_list):
    bootstrap_list = []

    sample_seq = ""
    rand_limit = len(fasta_list[0]) 
    length_hit = False

    i = 0
    while i < len(fasta_list):
        while not length_hit:
            col_num = random.randint(0, rand_limit)
            col =  get_column(fasta_list, col_num)
            if len(col) > (rand_limit - len(sample_seq)):
                col = col[ :rand_limit - len(sample_seq)]
                length_hit = True 
            sample_seq += col
        bootstrap_list.append(sample_seq)
        i += 1
    return bootstrap_list


'''
Helper function that returns a column 
'''

def get_column(fasta_list, index):
    col_str = ""
    for seq in fasta_list:
        col_str += seq[index]
    return col_str


'''
boostrap_main - responsbile for 

'''