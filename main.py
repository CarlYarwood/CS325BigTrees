from sys import argv
from FASTA import getSeq
from newUPGMA import UPGMA
from Clade import Clade
from Alignment import globalAlign
def main():
    seq = getSeq(argv[1])
    newSeq = globalAlign(seq)
    startTree = UPGMA(newSeq)
    print(startTree[0].generateStringRep())
    return
main()
