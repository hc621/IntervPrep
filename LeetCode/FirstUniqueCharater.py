s = "loveleetcode"
s = "loveleetcodeloveleetcode"

def firstUniqChar(s):

    uniqueList = [c for c in set(s) if s.count(c)==1]
    if len(uniqueList)==0:
        return -1
    else:
        indexList=[s.find(x) for x in uniqueList]
        return min(indexList)



print(firstUniqChar(s))