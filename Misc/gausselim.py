def gausselim(A, b):
    n = len(A)                          # Number of Rows
    m = len(A[0])                       # Number of Columns

    for i in range(n):                  # Iterates through rows
        norm = A[i][i]

        for j in range(m):              # Normalizes the ith row
            A[i][j] /= norm
        b[i] /= norm
        
        for k in range(i+1, n):         # Elimination step
            factor = A[k][i]/A[i][i]

            for l in range(m):          # lth row - ith row
                A[k][l] = A[k][l] - A[i][l]*factor
            b[k] = b[k] - b[i]*factor
        
    x = [0 for i in range(m)]           # Initiallising x to have all 0s

    x[n-1] = b[n-1]/A[n-1][n-1]
    for i in range(n-2, -1, -1):
        sum = 0
        for j in range(i+1, n):
            sum += A[i][j]*x[j]
        
        x[i] = (b[i] - sum)/A[i][i]

    return x
