import numpy as np
from Clade import Clade
from Clade import Leaf
import datetime
from dynamic_sequence_evaluator import dynamicAlignment
#only half done, feel under the weather, need to write the part of the method
#that puts together the new score matrix
def UPGMA(allignedSeqs):
    currentCladesAndLeafs = []
    print(len(allignedSeqs))
    print(datetime.datetime.now())
    for i in range(len(allignedSeqs)):
        currentCladesAndLeafs.append(Leaf(i))
    scoreMatrix = buildInitialScoreMatrix(allignedSeqs)
    for i in range(len(allignedSeqs)-1):
        print(i)
        print(datetime.datetime.now())
        #for c in scoreMatrix:
            #print(c)
        temp = buildNextMatrix(scoreMatrix,currentCladesAndLeaves)
        scoreMatrix = temp[0]
        currentCladesAndLeaves = temp[1]
        print(currentCladesAndLeaves.generateStringRep())
        #for c in scoreMatrix:
            #print(c)
    return currentCladesAndLeaves
def buildNextMatrix(scoreMatrix, CurrentCladesAndLeaves):
    minimum = scoreMatrix[0][1]
    row = 0
    col = 1
    for i in range(len(scoreMatrix)):
        for c in range(len(scoreMatrix[i])):
            if scoreMatrix[i][c] < minimum and i != c:
                minimum = scoreMatrix[i][c]
                row = i
                col = c
    newScoreMatrix = []
    for i in range(len(scoreMatrix)):
        if i != max(row, col):
            newScoreMatrix.append([])
        for c in range(len(scoreMatrix[i])):
            if (i == min(row,col) or c == min(row,col)):
                newScoreMatrix.append(((CurrentCladesAndLeaves[col].weight * scoreMatrix[row][c]) + (CurrentCladesAndLeaves[col].weight *scoreMatrix[col][c]))/(CurrentCladesAndLeaves[row].weight + CurrentCladesAndLeaves[col].weight))
            elif i != max(row,col) or c != max(row,col):
                newScoreMatrix.append(scoreMatrix[i][c])        
    NewClade = Clade(CurrentCladesAndLeaves[i], CurrentCladesAndLeaves[c], scoreMatrix[row][col])
    CurrentCladesAndLeaves.remove(max(row,col))
    CurrentCladesAndLeaves.remove(min(row,col))
    CurrentCladesAndLeaves.insert(NewClade, min(row,col))
    rv = []
    rv.append(newScoreMatrix)
    rv.append(CurrentCladesAndLeaves)
    return rv
#this method is untested and cannot be truely tested until dynamic sequencing
#is done
def buildInitialScoreMatrix(allignedSeqs):
    scoreMatrix = []
    count = 0
    for i in range(len(allignedSeqs)):
        scoreMatrix.append([])
        for c in range(i,len(allignedSeqs)):
            temp = dynamicAlignment(allignedSeqs[i], allignedSeqs[c])#remove when global alignment is added
            scoreMatrix[i].append(k2pScore(temp[0], temp[1])) #replace temp[0] with allignedSeqs[i] and temp[1] with allignedSeqs[c] when global allignment is added
            print(count)
            count = count+1
    return scoreMatrix


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
    return (-0.5*np.log(1 - (2*(S/len(allignedSeq1))) - (V/len(allignedSeq1)))) - (0.25*np.log(1 - (2*(V/len(allignedSeq1)))))


def isTransition(base1, base2):
    if (isPurine(base1) and isPurine(base2)) or (isPyrimidine(base1) and isPyrimidine(base2)):
        return True
    else:
        return False
    return



def isTransversion(base1, base2):
    if (isPurine(base1) and isPyrimidine(base2)) or (isPyrimidine(base1) and isPurine(base2)):
        return True
    else:
        return False
    return

def isPurine(base):
    if base.upper() == "A" or base.upper() == "G":
        return True
    else:
        return False
    return




def isPyrimidine(base):
    if base.upper() == "T" or base.upper() == "C":
        return True
    else:
        return False
    return
