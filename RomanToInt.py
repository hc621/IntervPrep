s = 'III'
Input="LVIII"
Input= "MCMXCIV"

letterMap =  {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
subtr_lettrs = ['I', 'X', 'C']
minuend_lettrs = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
res = 0


for x in minuend_lettrs:
    while s.find(x) != -1:
        res += letterMap[x]
        if s.find(x) == 0:
            s = s[1:]
        else:
            loc = s.find(x)
            for z in s[0:loc]:
                res -= letterMap[z]
                s=s[loc+1:]


print(s)
print(res)