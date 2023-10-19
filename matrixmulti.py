Perform matrix multiplication
A = [1 , 2 , 3],[4 , 5 , 6]
B = [1 , 2 , 3],[4 , 5 , 6]
T = [0 , 0 ,0],[0 , 0 , 0]
for i in range (len(A)):
    for j in range (len (A[0])):
        for k in range (len (B)):
            T[i][j] += A[i][k]* B[k][j]
for r in T:
    print(r)
