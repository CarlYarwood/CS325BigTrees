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
The main method acts as a way to execute all the code on any hard coded
sequence. Much of this code was written for the functions to be used
elsewhere so values were assumed to be provided.
'''

def main():
    

    queary_list = ['-TATAAAA','-ATCGAT','-CAGCTG', '-GGTAAGT', '-GGTGAGT',
                   'GTAA','GTGA']

    seq = '-ACAGTA'
    queary_list = ['-CAGC']
    
    score_list = []

    for i in range(len(queary_list)):

        queary = queary_list[i]
        
        gene_comparison_matrix = initialize_gene_comparison_matrix\
                                 (seq, queary)
        gene_comparison_matrix = fill_gene_comparison_matrix\
                             (gene_comparison_matrix, seq, queary)

        traceback_data = traceback(gene_comparison_matrix, seq, queary)

        traceback_value = traceback_data[0]
        traceback_startpoint = traceback_data[1]
        traceback_endpoint = traceback_data[2]

        max_score = (len(queary) - 1) * match_bonus
        score = traceback_value/max_score
        score_list.append(score)

        print(gene_comparison_matrix)

        if (score >= .8):
            find_codon(seq, traceback_startpoint, traceback_endpoint)
    
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
This runs a semi-global traceback on a passed in 2D numpy array

Parameters: gene_comparison_matrix (2D numpy array) the 2d array being traced
            seq (string) the length of the string is used for iterators
            queary (string) the length of the string is used for iterators

Returns a list of traceback data. This list contains the score of the trace
the starting position of the trace, and the end position of the trace. 
'''

def traceback(gene_comparison_matrix, seq, queary):

    start_coordinate = 0

    for i in range(len(seq)):

         dummy = gene_comparison_matrix[i][len(queary) - 1]

         if( dummy >
             gene_comparison_matrix[start_coordinate][len(queary) - 1] ):
             start_coordinate = i

    traceback_value = gene_comparison_matrix[start_coordinate]\
                      [len(queary) - 1]
                       

    y_coordinate = start_coordinate
    x_coordinate = len(queary) - 1
    
    while x_coordinate != 0 and y_coordinate != 0 :

        left_score = gene_comparison_matrix[y_coordinate][x_coordinate - 1]
        upper_score = gene_comparison_matrix[y_coordinate - 1][x_coordinate]
        diagonal_score = gene_comparison_matrix[y_coordinate - 1]\
        [x_coordinate -1]

        max_value = max(left_score, upper_score, diagonal_score)

        if((diagonal_score == left_score or diagonal_score == upper_score)
            and max_value == diagonal_score):
            y_coordinate = y_coordinate - 1
            x_coordinate = x_coordinate - 1
            
        elif(left_score == upper_score and left_score > diagonal_score):
            y_coordinate = y_coordinate - 1

        elif(left_score == max_value):
            x_coordinate = x_coordinate - 1

        elif(upper_score == max_value):
            y_coordinate = y_coordinate - 1

        elif(diagonal_score == max_value):
            y_coordinate = y_coordinate - 1
            x_coordinate = x_coordinate - 1
            

    return [traceback_value, start_coordinate, y_coordinate]

if __name__ == '__main__': main()
