from functions import *
from secretpy import ColumnarTransposition as trans

while True:
    text = input("Enter text to decrypt: ")
    key = int(input("Enter key: "))
    dec = trans()
    outcome = dec.decrypt(boring(text), key)

    print("\n")
    print(outcome)
    print("\n")

## Returns an error lol not finsihed.
