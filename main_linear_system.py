from playLA.Matrix import Matrix
from playLA.Vector import Vector
from playLA.LinearSystem import LinearSystem


if __name__ == "__main__":

    A = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
    b = Vector([7, -11, 1])
    ls = LinearSystem(A, b)
    ls.gauss_jordan_elimination()
    ls.fancy_print()
    print()

    A2 = Matrix([[1, -1, 2, 0, 3],
                 [-1, 1, 0, 2, -5],
                 [1, -1, 4, 2, 4],
                 [-2, 2, -5, -1, -3],])
    b2 = Vector([1, 5, 13, -1])
    ls2 = LinearSystem(A2, b2)
    ls2.gauss_jordan_elimination()
    ls2.fancy_print()
    print()

    A3 = Matrix([[2, 2], [2, 1], [1, 2]])
    b3 = Vector([3, 2.5, 7])
    ls3 = LinearSystem(A3, b3)
    if not ls3.gauss_jordan_elimination():
        print("No solution!")
    ls3.fancy_print()
    print()

    A4 = Matrix([[2, 0, 1],
                 [-1, -1, -2],
                 [-3, 0, 1]])
    b4 = Vector([1, 0, 0])
    ls4 = LinearSystem(A4, b4)
    if not ls4.gauss_jordan_elimination():
        print("No Solution!")
    ls4.fancy_print()

