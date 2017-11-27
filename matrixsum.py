def matrixElementsSum(matrix):
    suml = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                suml = suml + matrix[i][j]
            else:
                for k in range(i, len(matrix)):
                    matrix[k][j] = 0
            
    return suml
