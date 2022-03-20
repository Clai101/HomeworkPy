from sys import stdin
from functools import reduce
from numpy import array, linalg


class MatrixError(BaseException):

    def __init__(self, matrix1, matrix2):

        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix(list):

    def __init__(self, *args, **kwargs):
        """Initialisation"""

        self.__matrix = args[0]
        return super().__init__(*args, **kwargs)

    def __str__(self):
        """Returns a matrix"""

        return '\n'.join('\t'.join(str(line[column]) for column in
                         range(len(line))) for line in self)

    def size(self):
        """Returns the size of a matrix"""

        return (len(self), len(self[0]))

    @property
    def get_line(self):
        """Returns the lines of a matrix"""

        return len(self)

    @property
    def get_column(self):
        """Returns the columns of a matrix"""

        return len(self[0])

    def __add__(self, added_matix):
        """Returns the sum of matrices"""

        if self.size() != added_matix.size():
            raise MatrixError(self, added_matix)
        uns = Matrix([[pair[0] + pair[1] for pair in zip(self[line],
                     added_matix[line])] for line in range(len(self))])
        return uns

    def transpose(self):
        """Transpose the matrix and returns it"""

        buff = [[self[line][column] for line in range(self.get_line)]
                for column in range(self.get_column)]
        self = self.__init__(buff)
        return Matrix(buff)

    @staticmethod
    def transposed(matrix):
        """Returns the transposed matrix"""

        return Matrix([[matrix[line][column] for line in
                      range(matrix.get_line)] for column in
                      range(matrix.get_column)])

    def __mul__(self, second_mul):
        """Returns the multiplication of matrices"""

        if type(second_mul) in [int, float]:
            return Matrix(list(map(lambda line: list(map(lambda point:
                          point * second_mul, line)), self)))
        elif type(second_mul) in [Matrix, SquareMatrix]:
            if self.get_column != second_mul.get_line:
                raise MatrixError(self, second_mul)
            uns = Matrix([[sum([second_mul[_][column] * self[line][_]
                         for _ in range(self.get_column)])
                         for column in range(second_mul.get_column)]
                         for line in range(self.get_line)])
            return uns
        else:
            raise NameError('Wrong data type')

    def solve(self, vector):
        """Solve  Returns the multiplication of matrices"""

        matrix = array(self)
        vector = array(vector)
        return list([_ for _ in linalg.solve(matrix, vector)])

    __rmul__ = __mul__


class SquareMatrix(Matrix):

    def __init__(self, *args, **kwargs):
        """Initialisation"""

        self.__matrix = args[0]
        for i in self.__matrix:
            if len(self.__matrix) != len(i):
                raise NameError('Wrong data type')
        return super().__init__(*args, **kwargs)

    def __pow__(self, num):
        """Raises a matrix to a power"""

        if num == 0:
            return SquareMatrix([[(0 if i != j else 1) for i in
                                range(self.get_column)] for j in
                                range(self.get_column)])
        elif num == 1:
            return self
        else:
            matrix = self
            for i in range(num - 1):
                matrix = matrix * self
            return matrix


exec(stdin.read())
