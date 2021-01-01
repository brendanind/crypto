## DWTFUL Licence

from functions import *

alphabet = "abcdefghijklmnopqrstuvwxyz"


## ord: char -> asciiNumber
## chr: asciiNumber -> char

## Function must have lowercase, non


def wheelShiftSolve(text, iOverride=False):
    results = {}
    for i in range(0,len(alphabet)): #Cycle through the 26? possible shifts that could have been done.

        if iOverride:
            i = iOverride-1 ## minus 1 since counts from zero not 1

        ## Where i is the shift amount
        ## print("shift by", i)
        output = ''
        for j in text:
            ## For each character:
            if (ord(j) + i) > 122: ##122 is the ord("z") val
                ## i.e. it needs to turn over.
                spillover = ((ord(j)+i) - ord("z"))
                ## print(spillover)
                output = output + chr(((ord("a")-1) + spillover))
            else:
                output = output + chr(ord(j) + i)
        results[i] = output

    return results

while True:

    print(wheelShiftSolve(boring(str(input("Enter Text: "))), False))