class Vector:

    def __init__(self, lst):
        # _values: internal variable
        self._values = list(lst)  # immutable

    def __add__(self, another):
        assert len(self) == len(another), \
            "Error in adding. Length of vectors must be same."
        return Vector([a + b for a, b in zip(self, another)])

    def __sub__(self, another):
        assert len(self) == len(another), \
            "Error in subtracting. Length of vectors must be same."
        return Vector([a - b for a, b in zip(self, another)])

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
