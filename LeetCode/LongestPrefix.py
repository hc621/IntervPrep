
strs=["flower","flow","flight"]
#str= ["dog","racecar","car"]
def longestCommonPrefix(strs):
    if not len(strs):
        return ''
    j = len(strs[0])
    for i in range(len(strs) - 1):
        first = strs[i]
        second = strs[i + 1]
        while first[:j] != second[:j]:
            j -= 1
    return strs[0][:j]

res = longestCommonPrefix(strs)
print(res)