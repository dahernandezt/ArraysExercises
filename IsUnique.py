import sys
def isUnique(chain):
    for i in range(len(chain)):
        for j in range(i,len(chain)):
            if (i != j and chain[i] == chain[j]):
                print("values {}, {}".format(i,j))
                return False
    return True              

if __name__ == "__main__":
    print(isUnique(sys.argv[1]))
