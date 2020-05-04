def number_of_differences(n,m, A, B):
    counter = 0
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                counter += 1
    return counter
