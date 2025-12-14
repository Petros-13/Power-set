import math

def printPowerSet(s, setSize):
    powerSetSize = int(math.pow(2, setSize))
    for outer in range(powerSetSize):
        for inner in range(setSize):
            if (outer & (1 << inner)) > 0:
                print(s[inner], end=" ")
        print()

size = int(input("Enter array size : "))
s = []

for i in range(size):
    n = int(input("Enter element : "))
    s.append(n)

printPowerSet(s, len(s))
