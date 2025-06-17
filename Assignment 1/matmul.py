# Funciton to multiply 2 matrices (takes 2 matrices as input and returns 1 matrix as output)
def matrix_multiply(matrix1, matrix2):

    # To test if any of the matrices are empty
    if (not matrix1) or (not matrix2):
        raise ValueError("One of the matrices is empty")

    # Storing the dimentions of the matrices as tuples
    size1 = (len(matrix1), len(matrix1[0]))
    size2 = (len(matrix2), len(matrix2[0]))

    # Checking if the dimentions mismatch
    if size1[1] != size2[0]:
        raise ValueError("Matrices have incompatible dimentions")
    
    # Checking if every element in matrix1 is a number
    for i in range(size1[0]):
        for j in range(size1[1]):
            if isinstance(matrix1[i][j], (int, float)):
                continue
            raise TypeError("Not every element in matrix1 is a number")
    
    # Checking if every element in matrix1 is a number
    for i in range(size2[0]):
        for j in range(size2[1]):
            if isinstance(matrix2[i][j], (int, float)):
                continue
            raise TypeError("Not every element in matrix2 is a number")


    # Performing the actual matrix multiplication
    # i runs through the length of rows of matrix1
    # j runs through the length of columns of matrix1
    # k runs through the length of columns of matrix2
    matrix_out = []
    for i in range(size1[0]):
        row = []

        # Creating the ith row then appending it to matrix_out
        for k in range(size2[1]):
            element = 0
            
            for j in range(size1[1]):
                # Calculating the value of the element at the (i, k)th position in matrix_out
                element += matrix1[i][j] * matrix2[j][k]
            row.append(element)

        matrix_out.append(row)
        
    return matrix_out

