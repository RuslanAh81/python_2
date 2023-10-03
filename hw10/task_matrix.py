

class Matrix:
    def __init__(self, mat_list):
        self.mat = mat_list

    def get_matrix(self):
        return self.mat

    def transpon_mat(self):
        matrix_output = [[0 for _ in range(len(self.mat))] for _ in range(len(self.mat[0]))]
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                matrix_output[j][i] = self.mat[i][j]
        return matrix_output

    def print_matrix(self):
        return '\n'.join(str(x) for x in self.mat)

    def print_transpon_matrix(self):
        return '\n'.join(str(x) for x in self.transpon_mat())


if __name__ == '__main__':
    _mat = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    print(_mat.print_matrix())
    print()
    print(_mat.print_transpon_matrix())


