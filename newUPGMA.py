import numpy as np
from Clade import Clade
from Clade import Leaf
def UPGMA(seqs):
    Matrix = buildInitMatrix(seqs)
    clades = []
    for i in range(len(seqs)):
        clades.append(Leaf(i))
    for i in range(len(seqs) - 1):
        temp = buildNextMatrix(clades, Matrix)
        Matrix = []
        clades = []
        clades = temp[0]
        Matrix = temp[1]
    return clades

#I count the gaps just so that if we choose we can account for them

def k2pScore(allignedSeq1, allignedSeq2):

    S = 0

    V = 0

    Gaps = 0

    print(f"1: {len(allignedSeq1)} 2: {len(allignedSeq2)}") 

    for i in range(min(len(allignedSeq2), len(allignedSeq1))):

        if isTransition(allignedSeq1[i],allignedSeq2[i]): # lol maybe just take the min when doing this?

            S = S + 1

        elif isTransversion(allignedSeq1[i],allignedSeq2[i]):

            V = V + 1

        elif allignedSeq1[i] == "-" or allignedSeq2[i] == "-":

            Gaps = Gaps + 1

    

    #-------------------------New Stuff

    if(S >= 0.25):

        S = 0


    if(V >= 0.5):

        V = 0

    

    if(S == 0 and V == 0):

        print("Sequences have too much variance for useful knowledge and this"+\

              " algorithm does not have rarer mutation detection implemented")

    #---------------------------------------------

    return (-0.5*np.log(1 - (2*(S/len(allignedSeq1))) - (V/len(allignedSeq1)))) - (0.25*np.log(1 - (2*(V/len(allignedSeq1)))))
def dc(seq1,seq2):
    gap = 0
    if(len(seq1) == len(seq2)):
        print("allined seq")
        num = len(seq1)
        diff = 0
        for i in range(num):
            if seq1[i] != seq2[i] and (seq1[i] != "-" and seq2[i] != "-") :
                diff = diff + 1
            elif seq1[i] == "-" or seq2[i] == "-":
                gap = gap + 1
        return -0.75 * np.log(1 - (float(diff)/float(num-gap)))
    else:
        print("unalligned seq")
        num = min(len(seq1),len(seq2))
        diff = 0
        for i in range(num):
            if seq1[i] != seq2[i] and (seq1[i] != "-" and seq2[i] != "-") :
                diff = diff + 1
            elif seq1[i] == "-" or seq2[i] == "-":
                gap = gap + 1
        return -0.75 * np.log(1 - (float(diff)/float(num - gap)))
def buildInitMatrix(seqs):
    initMatrix = []
    for i in range(len(seqs)):
        initMatrix.append([])
        for c in range(len(seqs)):
            initMatrix[i].append(dc(seqs[i], seqs[c]))
    return initMatrix
def buildNextMatrix(clades, prevMatrix):
    mini = prevMatrix[0][1]
    row = 0
    col = 1
    for i in range(len(prevMatrix)):
        for c in range(len(prevMatrix[i])):
            if prevMatrix[i][c] < mini and i != c:
                mini = prevMatrix[i][c]
                row = i
                col = c
    newMatrix = []
    minPos = min(row, col)
    maxPos = max(row, col)
    count = -1
    for i in range(len(prevMatrix)):
        if i != maxPos :
            newMatrix.append([])
            count = count + 1
        for c in range(len(prevMatrix[i])):
            if (i == minPos or c == minPos) and (i != maxPos and c!= maxPos):
                newMatrix[count].append(float((clades[row].weight * prevMatrix[row][c]) + (clades[col].weight * prevMatrix[i][col]))/float(clades[row].weight + clades[col].weight))
            elif i != maxPos and c != maxPos:
                newMatrix[count].append(prevMatrix[i][c])
    newClade = Clade(clades[row], clades[col], prevMatrix[row][col])
    clades.remove(clades[maxPos])
    clades.remove(clades[minPos])
    clades.insert(minPos, newClade)
    rv = [clades, newMatrix]
    return rv
