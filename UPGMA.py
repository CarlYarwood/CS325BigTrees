import numpy as np




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
        return true
    else:
        return false
    return



def isTransversion(base1, base2):
    if (isPurine(base1) and isPyrimidine(base2)) or (isPyrimidine(base1) and isPurine(base2)):
        return true
    else:
        return false
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
