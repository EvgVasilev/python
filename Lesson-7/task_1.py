class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            s = s + ' '.join(map(str, self.matrix[i])) + '\n'
        return s

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        res = self.matrix
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                res[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(res)


l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
first = Matrix(l1)
second = Matrix(l2)
print(f'Первая матрица:\n{first}')
print(f'Вторая матрица:\n{second}')
result = first + second
print(f'Сумма матриц:\n{result}')
