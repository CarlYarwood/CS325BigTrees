from sys import argv
from FASTA import getSeq
from UPGMA import UPGMA
from Clade import Clade
def main():
    seq = getSeq(argv[1])
    print(len(seq))
    newseq = []
    startTree = UPGMA(seq)
    print(startTree[0].generateStringRep())
    return
main()
