def min_operations(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
    
    operations = []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and dp[i][j] == dp[i-1][j] + 1:
            operations.append(('remove', s1[i-1]))
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j-1] + 1:
            operations.append(('insert', s2[j-1]))
            j -= 1
        else:
            if s1[i-1] != s2[j-1]:
                operations.append(('replace', s2[j-1]))
            i -= 1
            j -= 1
    
    return (dp[m][n], list(reversed(operations)))
s1 = 'eman'
s2 = 'ebas'
print(min_operations(s1, s2)) 

s3 = 'intention'
s4 = 'execution'
print(min_operations(s3, s4))