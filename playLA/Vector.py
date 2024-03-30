class Vector:

    def __init__(self, lst):
        # _values: internal variable
        self._values = list(lst)  # immutable

    def __getitem__(self, idx):
        return self._values[idx]

    def __len__(self):
        # return length of Vector
        return len(self._values)

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))
