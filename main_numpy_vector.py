import numpy as np

if __name__ == "__main__":

    print(np.__version__)

    lst = [1, 2, 3]
    lst[0] = "Liner Algebra"
    print(lst)

    # np.array's creation
    vec = np.array([1, 2, 3])
    print(vec)
    # vec[0] = "linear algebra"  # error!
    # vec[0] = 27  # correct, mutable
    # print(vec)

    print(np.zeros(3))
    print(np.ones(3))
    print(np.full(3, 66))

    # np.array's attributes
    print(vec)
    print("size =", vec.size)
    print("size =", len(vec))
    print(vec[0])
    print(vec[-1])  # the last element
    print(vec[0: 2])  # python's slice
    print(type(vec[0: 2]))

    # np array's basic operations
    vec2 = np.array([4, 5, 6])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))
    print("{} * {} = {}".format(vec, 3, vec * 3))
    print("{} * {} = {}".format(3, vec, 3 * vec))
    print("{} * {} = {}".format(vec, vec2, vec * vec2))
    print("{} dot product {} = {}".format(vec, vec2, vec.dot(vec2)))

    print("norm({}) = {}".format(vec, np.linalg.norm(vec)))
    print("normalize({}) = {}".format(vec, vec / np.linalg.norm(vec)))
    print(np.linalg.norm(vec / np.linalg.norm(vec)))  # should return 1

    zero3 = np.zeros(3)
    # zero3 / np.linalg.norm(zero3)  # zero division error

