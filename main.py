from sys import argv
from FASTA import getSeq
from UPGMA import UPGMA
from Clade import Clade
def main():
    seq = getSeq(argv[1])
    newseq = []
    startTree = UPGMA(seq)
    startTree[0].generateStringRep()
    return
main()
