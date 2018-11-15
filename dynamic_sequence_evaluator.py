import numpy as np

'''
The following program takes in a DNA sequence and returns likely open reading
frames. To do this we first calculate the semi-global alignment of the frame
and the queary in question. Then we calculate which frame has the highest
match based on the value of the frame and the closest match found with the
given queary.

The penalties were chosen because they were the in class examples and that
made it easier to debug my program.

'''

gap_penalty = -7

mismatch_penalty = -4

match_bonus = 5

'''
The dynamicAlignment method acts as a way to execute all the code on 
any hard coded sequence. Much of this code was written for 
the functions to be used elsewhere so values were assumed to be provided.
'''

def dynamicAlignment(seq1, seq2):
    
##
##    for i in range(len(queary_list)):
##
##        queary = queary_list[i]
        
    gene_comparison_matrix = initialize_gene_comparison_matrix\
                             (seq1, seq2)
    gene_comparison_matrix = fill_gene_comparison_matrix\
                         (gene_comparison_matrix, seq1, seq2)

    traceback_data = traceback(gene_comparison_matrix, seq1, seq2)

    traceback_value = traceback_data[0]
    aligned_seq1 = traceback_data[1]
    aligned_seq2 = traceback_data[2]
    return [aligned_seq1, alignedseq2]


'''
Initializes a global alignment matrix.

Parameters: seq (string) this is the sequence to be matched.
            queary (string) this is the string being compared to the sequence

Returns a 2D matrix with the first row and column filled with the gap penalty
'''


def initialize_gene_comparison_matrix(seq, queary):
    gene_comparison_matrix = np.zeros([len(seq),len(queary)], dtype=int)

    for i in range(len(seq)):

        if( i != 0 ):
            gene_comparison_matrix[i][0] = gene_comparison_matrix[i - 1][0] \
                                           + gap_penalty

    for j in range(len(queary)):

        if( j != 0 ):
            gene_comparison_matrix[0][j] = gene_comparison_matrix[0][j - 1] \
            + gap_penalty

    return gene_comparison_matrix

'''
Fills global alignment matrix.

Parameters: gene_comparison_matrix (2D numpy array) this is what is filled in
            seq (string) the length of the string is used for iterators
            queary (string) the length of the string is used for iterators

Returns a 2D matrix with every value filled in
'''

def fill_gene_comparison_matrix(gene_comparison_matrix, seq, queary):

    left_score = 0
    upper_score = 0
    diagonal_score = 0
 
    for i in range(len(seq)):
        for j in range(len(queary)):
          
            if( i and j != 0):

                upper_score = gene_comparison_matrix[i][j - 1]
                left_score = gene_comparison_matrix[i - 1][j]
                diagonal_score = gene_comparison_matrix[i -1][j -1]

                if( seq[i] == queary[j]):
                    gene_comparison_matrix[i][j] = \
                    max(left_score + gap_penalty, upper_score + gap_penalty,
                        diagonal_score + match_bonus)
                    
                else:
                     gene_comparison_matrix[i][j] = \
                     max(left_score + gap_penalty, upper_score + gap_penalty,
                        diagonal_score + mismatch_penalty)
    
    return gene_comparison_matrix


'''
This runs a global traceback on a passed in 2D numpy array

Parameters: gene_comparison_matrix (2D numpy array) the 2d array being traced
            seq1 (string) the length of the string is used for iterators
            seq2 (string) the length of the string is used for iterators

Returns a list of traceback data. This list contains the score of the trace
seq1 with added in gaps, and seq2 with added in gaps. 
'''

def traceback(gene_comparison_matrix, seq1, seq2): 
             
    y_coordinate = len(seq1) - 1
    x_coordinate = len(seq2) - 1
    aligned_seq1 = seq1[1:len(seq1)]
    aligned_seq2 = seq2[1:len(seq2)]
    
    traceback_value = gene_comparison_matrix[ y_coordinate]\
                      [x_coordinate]
    while True:
        print("X_coordinate = " + str(x_coordinate) + " y_coordinate = " + str(y_coordinate))
        current_score = gene_comparison_matrix[y_coordinate][x_coordinate]
        
        if(x_coordinate != 0 and y_coordinate !=0):
            left_score = gene_comparison_matrix[y_coordinate]\
                         [x_coordinate - 1]
            upper_score = gene_comparison_matrix[y_coordinate - 1]\
                          [x_coordinate]
            diagonal_score = gene_comparison_matrix[y_coordinate - 1]\
            [x_coordinate -1]
        else:
            #end condition
            if(x_coordinate == 0 and y_coordinate == 0):
                return [traceback_value, aligned_seq1, aligned_seq2]
            #only move up
            elif(x_coordinate == 0 and y_coordinate != 0):
                upper_score = gene_comparison_matrix[y_coordinate - 1]\
                          [x_coordinate]
                left_score = upper_score - 1
                diagonal_score = upper_score -1
            #only move right
            elif(x_coordinate != 0 and y_coordinate == 0):
                left_score = gene_comparison_matrix[y_coordinate]\
                         [x_coordinate - 1]
                upper_score = left_score - 1
                diagonal_score = left_score - 1

        #move diagonal
        if(current_score - diagonal_score == match_bonus and seq2[x_coordinate] == seq1[y_coordinate]):
            x_coordinate = x_coordinate - 1
            y_coordinate = y_coordinate - 1
        elif(current_score - diagonal_score == mismatch_penalty):
            x_coordinate = x_coordinate - 1
            y_coordinate = y_coordinate - 1
        #move up
        elif(current_score - upper_score == gap_penalty):
            y_coordinate = y_coordinate - 1
            aligned_seq2 = aligned_seq2[:x_coordinate] + "-" + aligned_seq2[x_coordinate:]
        #move left
        elif(current_score - left_score == gap_penalty):
            x_coordinate = x_coordinate - 1
            x_coordinate = x_coordinate - 1
            aligned_seq1 = aligned_seq1[:y_coordinate] + "-" + aligned_seq2[y_coordinate:]
        else:
            print("An error has occured")


            
def main():
    dynamicAlignment( "-ACAGTA","-CAGC")

if __name__ == '__main__': main()
