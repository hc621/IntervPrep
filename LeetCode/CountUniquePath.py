
# start from  (0,0) count how many unique path, you can arrive (m,n)

def numberOfPaths(p, q):
    # Create a 1D array to store
    # results of subproblems
    dp = [1 for i in range(q)]
    for i in range(p - 1):
        for j in range(1, q):
            dp[j] += dp[j - 1]
    return dp[q - 1]


# Driver Code
print(numberOfPaths(3, 3))