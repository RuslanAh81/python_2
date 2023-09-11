#  Напишите функцию для транспонирования матрицы

def transp_matrix(matrix_input: list):
    trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix


matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix)
print(transp_matrix(matrix))
