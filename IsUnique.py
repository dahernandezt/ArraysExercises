import sys
def isUnique(chain):
    chars = [False]*256
       
    for s in chain:
       if chars[ord(s)] == True:
           return False
       else:
           chars[ord(s)] = True         
    return True              

if __name__ == "__main__":
    print(isUnique(sys.argv[1]))
