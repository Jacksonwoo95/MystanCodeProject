"""
File: complement.py
Name:吳禹
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    make a func build_complement(dna)
    put str value to dna
    set s as a str, start with str('')
    do for loop
    """
    s = build_complement(str())
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    :param dna: str, DNA strand
    :return: str, complement strand of a DNA sequence
    """
    s = ''
    # :param s: str(), start with str('')
    if str(dna) == '':
        s = str('DNA strand is missing.')
    else:
        for i in range(len(dna)):
            if dna[i] == str('A'):
                s += str('T')
            elif dna[i] == str('T'):
                s += str('A')
            elif dna[i] == str('G'):
                s += str('C')
            elif dna[i] == str('C'):
                s += str('G')
    return s


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
