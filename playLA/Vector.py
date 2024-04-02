import math
from ._global import is_zero


class Vector:

    def __init__(self, lst):
        # _values: internal variable
        self._values = list(lst)  # immutable

    @classmethod
    def zero(cls, dim):
        # return zero vector of dim dimension
        return cls([0] * dim)

    def norm(self):
        # return norm of vector
        return math.sqrt(sum(e**2 for e in self))

    def normalize(self):
        if is_zero(self.norm()):
            raise ZeroDivisionError("Normalize error! Norm of vector is zero.")
        return self / self.norm()

    def underlying_list(self):
        return self._values[:]  # immutable

    def __add__(self, another):
        assert len(self) == len(another), \
            "Error in adding. Length of vectors must be same."
        return Vector([a + b for a, b in zip(self, another)])

    def __sub__(self, another):
        assert len(self) == len(another), \
            "Error in subtracting. Length of vectors must be same."
        return Vector([a - b for a, b in zip(self, another)])

    def dot(self, another):
        # dot product
        assert len(self) == len(another), \
            "Error in dot product. Length of vectors must be same."
        return sum(a * b for a, b in zip(self, another))

    def __mul__(self, k):
        # return self * k
        return Vector([e * k for e in self])

    def __rmul__(self, k):
        # return k * self
        return self * k

    def __truediv__(self, k):
        return (1 / k) * self

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self

    def __iter__(self):
        return self._values.__iter__()

    def __getitem__(self, idx):
        return self._values[idx]

    def __len__(self):
        # return length of Vector
        return len(self._values)

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))
