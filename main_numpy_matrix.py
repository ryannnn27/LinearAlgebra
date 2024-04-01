import numpy as np

if __name__ == "__main__":

    # creation of matrix
    A = np.array([[1, 2], [3, 4]])
    print(A)

    # attributes of matrix
    print(A.shape)
    print(A.T)

    # get element from matrix
    print(A[0][0])
    print(A[0])  # row vector
    print(A[0, :])
    print(A[:, 0])  # column vector

    # basic operations of matrix
    B = np.array([[5, 6], [7, 8]])
    print("A + B = {}".format(A + B))
    print("A - B = {}".format(A - B))
    print("10 * A = {}".format(10 * A))
    print("A * 10 = {}".format(A * 10))
    print("A * B = {}".format(A * B))
    print("A.dot(B) = {}".format(A.dot(B)))

    # A: [[1, 2], [3, 4]]
    v = np.array([10, 100])  # vector
    print("A + v = {}".format(A + v))
    print("A + 1 = {}".format(A + 1))

    print("A.dot(v) = {}".format(A.dot(v)))

    # identity matrix
    I = np.identity(2)
    print("I = {}".format(I))
    print("A.dot(I) = {}".format(A.dot(I)))
    print("I.dot(A) = {}".format(I.dot(A)))

    # inverse matrix
    invA = np.linalg.inv(A)
    print("invA = {}".format(invA))
    print("A.dot(invA) = {}".format(A.dot(invA)))
    print("invA.dot(A) = {}".format(invA.dot(A)))

    C = np.array([[1, 2, 3], [4, 5, 6]])
    # np.linalg.inv(C)  # error! only square matrix has inverse matrix
