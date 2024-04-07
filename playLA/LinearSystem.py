from .Vector import Vector
from ._global import is_zero
from .Matrix import Matrix


class LinearSystem:

    def __init__(self, A, b):

        assert A.row_num() == len(b), \
            "row number of A must be equal to the length of b."
        self._m = A.row_num()
        self._n = A.col_num()

        # Ab is augmented matrix
        if isinstance(b, Vector):
            self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]])
                       for i in range(self._m)]
        if isinstance(b, Matrix):
            self.Ab = [Vector(A.row_vector(i).underlying_list() + b.row_vector(i).underlying_list())
                       for i in range(self._m)]
        # save column of pivot
        self.pivots = []

    def _max_row(self, index_i, index_j, n):
        # compare abs value in case swap 0 and negative number wrongly
        best, row_num = abs(self.Ab[index_i][index_j]), index_i
        for i in range(index_i + 1, n):
            if abs(self.Ab[i][index_j]) > best:
                best, row_num = abs(self.Ab[i][index_j]), i
        return row_num

    def _forward(self):

        i, k = 0, 0
        while i < self._m and k < self._n:
            # see if Ab[i][k] is a pivot
            max_row = self._max_row(i, k, self._m)
            if max_row != i:
                # swap
                self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]

            if is_zero(self.Ab[i][k]):
                k += 1
            else:
                self.Ab[i] = self.Ab[i] / self.Ab[i][k]  # set pivot to 1
                for j in range(i + 1, self._m):
                    self.Ab[j] = self.Ab[j] - self.Ab[j][k] * self.Ab[i]
                self.pivots.append(k)
                i += 1
                k += 1

    def _backward(self):

        n = len(self.pivots)
        for i in range(n - 1, -1, -1):
            k = self.pivots[i]
            # Ab[i][k] is pivot
            for j in range(i - 1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[j][k] * self.Ab[i]

    def gauss_jordan_elimination(self):

        self._forward()
        self._backward()

        # if there is a solution, return true then false
        for i in range(len(self.pivots), self._m):
            if not is_zero(self.Ab[i][-1]):
                return False
        return True

    def fancy_print(self):

        for i in range(self._m):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n)), end=" ")
            print("|", self.Ab[i][-1])


def inv(A):

    if A.row_num() != A.col_num():
        return None

    n = A.row_num()
    ls = LinearSystem(A, Matrix.identity(n))
    ls.gauss_jordan_elimination()
    # todo: if there is a solution?
    invA = [[row[i] for i in range(n, 2 * n)] for row in ls.Ab]
    return Matrix(invA)
