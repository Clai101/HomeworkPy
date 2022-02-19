from sys import stdin

class Matrix:
    def __init__(self, *args, **kwargs):
        matrix = args[0]
        if (type(matrix) != list):
            raise MyException("Expected another type")     
        else:
            self.__columns = len(args[0][0])
        for line in matrix:
            if (type(line) != list):
                raise MyException("Expected another type")
        else:
            self.__lines = len(args[0])
        self.__matrix = matrix

    def __get_list(self):
        return self.__matrix

    def __str__(self):
        """Returns a matrix"""
        return '\n'.join('\t'.join(str(line[column]) for column in range(len(line))) for line in self.__matrix)

    @property
    def size(self):
        """Returns the size of a matrix"""
        return (self.__lines, self.__columns)

    def __add__(self, added_matix):
        """Returns the sum of matrices"""
        if ((self.__lines, self.__columns) != added_matix.size):
            raise MyException("Expected another type")
        uns = []
        for line in range(len(self.__matrix)):
            uns.append([])
            for pair in zip(self.__matrix[line], added_matix.__get_list[line]):
                uns[-1].append(pair[0] + pair[1])
        return Matrix(uns)

    @property
    def transpose(self):
        """Transpose the matrix"""
        transposed = [[0]*(self.__lines)]*(self.__columns)
        for line in range(self.__lines):
            for column in range(self.__columns):
                transposed[column][line] = self.__matrix[line][column]
        self.__matrix = transposed
        return self.__matrix

    @staticmethod
    def transposed(matrix):
        transposed = [[0]*(self.__lines)]*(self.__columns)
        for line in range(self.__lines):
            for column in range(self.__columns):
                transposed[column][line] = self.__matrix[line][column]
        return transposed

    def __mul__ (self, second_mul):
        """Returns the multiplication of matrices"""
        if (type(second_mul) in [int, float]):
            return Matrix(list(map(lambda line: list(map(lambda point: point * num, line)),self.__matrix)))
        elif (type(second_mul) in [Matrix,]):
            if self.__columns != second_mul.size()[0]:
                raise MyException("Expected another size")
            uns = [[0]*self.__lines]*second_mul.size[1]
            second_mul.transpose
            second_mul_l = second_mul.get_list
            for line in range(self.__lines):
                for column in range(second_mul.size()[1]):
                    for i in range(self.__columns):
                        uns[line][column] += second_mul[column] * self.__lines
            second_mul.transpose
            return uns

    __rmul__ = __mul__


m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)


exec(stdin.read())