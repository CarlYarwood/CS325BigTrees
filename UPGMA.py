import numpy as np
from Clade import Clade
from Clade import Leaf 
#only half done, feel under the weather, need to write the part of the method
#that puts together the new score matrix
def buildNextMatrix(scoreMatrix, CurrentCladesAndLeaves):
    minimum = scoreMatrix[0][0]
    row = 0
    col = 0
    for i in range(len(scoreMatrix)):
        for c in range(len(scoreMatrix[i])):
            if scoreMatrix[i][c] < minimum and i != c:
                minimum = scoreMatrix[i][c]
                row = i
                col = c
    NewClade = Clade(CurrentCladesAndLeaves[i], CurrentCladesAndLeaves[c], scoreMatrix[row][col])
    CurrentCladesAndLeaves.remove(row)
    CurrentCladesAndLeaves.remove(col)
    CurrentCladesAndLeaves.insert(NewClade, newPos)
#this method is untested and cannot be truely tested until dynamic sequencing
#is done
def buildInitialScoreMatrix(allignedSeqs):
    scoreMatrix = []
    for i in range(len(allignedSeqs)):
        scoreMatrix = []
        for c in range(i+1,len(allignedSeqs)):
            scoreMatrix[i].append(k2pScore(allignedSeqs[i], allignedSeqs[c]))
    return scoreMatrix


#I count the gaps just so that if we choose we can account for them
def k2pScore(allignedSeq1, allignedSeq2):
    S = 0
    V = 0
    Gaps = 0
    for i in range(len(allignedSeq1)):
        if isTransition(allignedSeq1[i],allignedSeq2[i]):
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
