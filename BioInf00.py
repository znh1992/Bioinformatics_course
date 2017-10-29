#!/usr/bin/python3

import os, sys, re
def reverse(seq):
    """Return the sequence string in reverse order."""
    # make a list of letters from string
    seq = list(seq.upper())
    
    # reverse the list
    seq = reversed(seq)
    
    # join the letters of the list into string and return
    return ''.join(seq)

    
def complement(seq):
    """Return the complementary sequence string."""
    # dictionary setup for complement
    subst = {'A': 'T', 'T': 'A', 'G':'C', 'C':'G'}
    
    # make a list of letters from string
    seq = list(seq.upper())
    
    # for loop of the letters and call the base_complementary dictionary
    compl_str = []
    for i in range(len(seq)):
        compl_str.append(subst[seq[i]])
    
    # join the letters of the list into string and return
    return ''.join(compl_str)


def main():
    # get input sequence
    dna_seq = input('Type your DNA sequence : ')
    
    # check DNA letter (only ACGTacgt)
    for i in range(len(dna_seq)):
        if dna_seq[i].upper() not in ['A', 'T', 'C', 'G']:
            print("Character: " + dna_seq[i] + ' not in DNA Alphabet')
            sys.exit()

    # change it to upper case

    # call reverse function
    dna_seq = reverse(dna_seq)

    # call complement function
    dna_seq = complement(dna_seq)

    # print output
    print("Reverse complement DNA :", dna_seq)
    # exit the program
    sys.exit()

if __name__ == '__main__':
 main()

