# The method that prints all  
# possible strings of length k. 
# It is mainly a wrapper over  
# recursive function printAllKLengthRec() 
perms = []
raw = input("enter raw text: ")

toInput = []

for i in raw:
    toInput.append(i)

    
def perm(set, k): 
  
    n = len(set)  
    printAllKLengthRec(set, "", n, k) 
  
# The main recursive method 
# to print all possible  
# strings of length k 
def printAllKLengthRec(set, prefix, n, k): 
      
    # Base case: k is 0, 
    # print prefix 
    if (k == 0) : 
        perms.append(prefix) 
        return
  
    # One by one add all characters  
    # from set and recursively  
    # call for k equals to k-1 
    for i in range(n): 
  
        # Next character of input added 
        newPrefix = prefix + set[i] 
          
        # k is decreased, because  
        # we have added a new character 
        printAllKLengthRec(set, newPrefix, n, k - 1)

perm(toInput, len(toInput))


def findx(x):
    x = perms.index(str(x))
    return x

while True:
    findx(input("Enter term: "))
