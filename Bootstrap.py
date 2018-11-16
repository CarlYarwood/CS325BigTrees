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
from Clade import Clade
from Clade import Leaf
from collections import Counter
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
boostrap_main - responsbile for:
0. running original UPGMA algorithm
1. getting a bootstrap list of sequences
2. running UPGMA on it 
    - repeating the above until we hit iter_num
3. creating a confidence tree that compares to 


param -- iter_num: number of times we do steps one and two

Returns: 
'''
def bootstrap_main(iter_num):
    i = 0
    bootstrap_list = []
    while i < iter_num:

        # execute steps 2 and 3
        # compare it to what we found int step 0
        # add to "confidence tree" ? 


        i += 1 


'''
split - takes in a Clade and returns an
array of string represenations of differents
Param -- clade_str: the Clade
Returns: an array of string representations for different leaves
'''
def split(clade):
    print()
    

'''
Compare_Clades - takes in two clades
- one clade is a confidence clade
- The other clade is a normal clade

The function mutates conf value levels of the confidence clade and 
doesn't return anything. 
'''
def compare_clades(conf_clade, clade):
    # TODO write check_clade_similarity 
    if check_clade_similarity(conf_clade, clade):
        conf_clade.conf_val += 1

        compare_clades(conf_clade.child1, clade.child1)
        compare_clades(conf_clade.child2, clade.child2)
        # when 3 of the leaves are not matching, return false
    else:
        compare_clades(conf_clade.child1, clade.child2)
        compare_clades(conf_clade.child2, clade.child1)
        compare_clades(conf_clade.child1, clade.child2)
        compare_clades(conf_clade.child2, clade.child1)
    

    print()

'''
check_clade_similarity - checks if two clades have the same elements on
the same levels 

-clade1 is 


-Returns True or False
'''
def check_clade_similarity(conf_clade, clade):
    #sim = False
    conf_clade_str = conf_clade.generateStringRep()
    clade_str = clade.generateStringRep()

    if conf_clade_str == clade_str:
        return True    






'''
TODO create function that runs throug original upgma tree collecting
confidence levels per clade 
each time a bootstrap tree is run, we need to check if any of the clades from
the original tree are in there and add accordingly 
'''