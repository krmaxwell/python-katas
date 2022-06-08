Write a program to convert Roman numerals into their Arabic equivalent.

INPUT REQUIREMENTS

Read one or more Roman numerals from standard input. Process one line at a time. Each input line contains only one Roman numeral, starting in column one. Assume the characters are all upper case with no embedded blanks.

OUTPUT REQUIREMENTS

The Arabic equivalent of each input Roman numeral is displayed on standard output, starting in column one.

FUNCTIONAL REQUIREMENTS

Here are the Arabic equivalents for Roman symbols:

The "basic" Roman symbols                                 The "auxiliary" Roman symbols
 

    I         X      C       M                                       V     L      D

    1        10     100    1000                                      5     50     500


Convert the Roman numeral to Arabic processing the symbols from left to right according to the following rules:
1. A symbol following one of greater or equal value adds to its value. (e.g., XII = 12)
2. A symbol preceding one of greater value subtracts its value. (e.g., IV = 4; XL = 40)


ERROR HANDLING REQUIREMENTS

In each of the error conditions below, display the given message and skip the numeral and continue processing the next line.

"Invalid character in input. Valid characters are I,V,X,L,C,D,M."
Only the listed characters are valid.

"Invalid numeral: can't subtract auxiliary symbol."
It is not permitted to subtract an "auxiliary" symbol. (CML, not LM = 950; XLV not VL, = 45).

"Invalid numeral: two consecutive subtractions."
Can't do two subtractions in a row, thus LIVX is illegal.

"Invalid numeral: additions don't decrease."
Additions must decrease, as you go from left to right. Thus, each symbol added must have a value equal or less than the last symbol which was added. Thus, LIIX is wrong, cause we added L, added I, subtracted I, then try to add X.
