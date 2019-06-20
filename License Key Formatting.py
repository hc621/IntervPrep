S = "5F3Z-2e-9-w"
K = 4

'''
S = "2-5g-3-J"
K=2
S = "2-4A0r7-4k"
K = 4

'''

def licenseKeyFormatting(S, K):
    t= S.replace('-','')[::-1]
    res=("-").join([t[i:i+K].upper() for i in range(0,len(t),K)])
    return res[::-1]


res =licenseKeyFormatting(S, K)
print(res)

