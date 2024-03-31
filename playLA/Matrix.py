
class Matrix:

    def __init__(self, list2d):
        # omit parameter validation
        self._values = [row[:] for row in list2d]  # immutable

    def __getitem__(self, pos):
        # get matrix's element from position
        r, c = pos
        return self._values[r][c]

    def shape(self):
        # m * n
        return len(self._values), len(self._values[0])

    def size(self):
        r, c = self.shape()
        return r * c

    def row_num(self):
        return self.shape()[0]

    __len__ = row_num

    def col_num(self):
        return self.shape()[1]

    def __repr__(self):
        return "Matrix({})".format(self._values)

    __str__ = __repr__
