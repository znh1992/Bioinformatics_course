#!/usr/bin/python3

# installed pip for python3 via https://gist.github.com/saurabhshri/46e4069164b87a708b39d947e4527298
# local installed biopython

import os, sys, re
from Bio.Seq import Seq

def main():
    # get input sequence
    dna_seq = input('Type your DNA sequence : ')

    # Seq object call
    dna_seq = Seq(dna_seq)
    
    # call reverse_complement function in Bio.Seq
    dna_seq = dna_seq.reverse_complement()
    
    # print output
    print("Reverse complement DNA :", dna_seq)

    # exit the program
    sys.exit()

if __name__ == '__main__':
    main()

