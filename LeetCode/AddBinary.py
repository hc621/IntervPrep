a='1111'
b='1111'

a = int(a, 2)
b = int(b, 2)
print( str(bin(a + b))[2:])


'''
tempSum = str(int(a) + int(b))

N = len(tempSum)
for i in range(N):
    # print(N-i-1)
    print(tempSum[N - i - 1])
    if tempSum[N - i - 1] == str(2) or tempSum[N - i - 1] == str(3):
        tempSum = str(int(tempSum) + 10 ** (i + 1) - 2 * 10 ** (i))
        print(tempSum)


print(tempSum)

'''