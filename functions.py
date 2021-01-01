## Brendan Ind
## DWTFUL Licence

## use:
## from functions import *
## to use these functions in other scripts

from itertools import permutations
from secretpy import Vigenere

def factors(number):
    '''
    Finds the factors of a give number
    e.g. print(factors(5)) returns an array [1,5]
         print(factors(6)) returns an array [1,2,3,6]
    '''

    out = []
    for i in range(int(number)):
        if int(number % (i + 1)) == int(0):
            print(str(i + 1), "is a factor of", number)
            out.append(i + 1)
    return out


def boring(text):
    '''
    Function that removes any characters which are not explicitly
    within a set of ascii codes. Will remove any punctuation and
    will also make letters lowercase.
    boring("HeLLo !") will return "hello"
    '''

    final = ""
    for i in text:
        letter = i.lower()
        asciiVal = ord(letter)
        if (int(asciiVal) > 122) or (asciiVal < 65) or ((asciiVal >= 91) and (asciiVal <= 96)):
            letter = ""
        else:
            final = final + letter
    ## print("plain:", final)
    return final


def split(text, length):
    '''
    split a large string into an array of small string of n length
    e.g. split("hello", 2) returns "he ll o"
    '''

    n = length
    array = [text[i:i + n] for i in range(0, len(text), n)]
    text = ''
    counter = -1
    for i in array:
        counter = counter + 1
        text = (str(text) + str(array[counter]) + " ")
    print("split into", length, "parts, the result is: ")
    print(text)
    return text


def turn(string):
    '''
    Puts text backwards
    '''

    ListOfAll = []
    newArray = []
    for i in string:
        ListOfAll.append(i)

    x = len(ListOfAll)
    for i in range(x):
        newArray.append(ListOfAll.pop(len(ListOfAll) - 1))
    finalText = ""
    dump = []
    x = len(newArray)
    for i in range(x):
        finalText = finalText + newArray[0]
        dump.append(newArray.pop(0))
    print("backwards: ")
    print(finalText)
    return finalText


def perm(text):
    '''
    Returns a list of all the word in every order that they could ever be arranged
    '''

    listOfPerms = []
    word = ""
    for i in permutations(text):  ## This will give us a list of each individual world perm
        ## print("i", i)
        word = ""
        for j in i:  ## for each char in the list that makes up a word, we add it to a string to make a string word.
            ## print("j", j)
            ## print(word)
            word = word + j
        listOfPerms.append(word)
        ## print(i)

    print("All Perms:")
    print(listOfPerms)
    return listOfPerms

def linearSearch(list1, required):
    position = 0
    for i in list1:
        position = position + 1
        if i == required:
            print("Found! Pos:"+str(position))
            return position
    print("Not found....")
    return False