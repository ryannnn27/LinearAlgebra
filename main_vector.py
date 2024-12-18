from playLA.Vector import Vector

if __name__ == "__main__":

    vec = Vector([5, 2])
    print(vec)
    print(len(vec))
    print("vec[0] = {}, vec[1] = {}".format(vec[0], vec[1]))

    vec2 = Vector([3, 1])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))

    print("{} * {} = {}".format(vec, 3, vec * 3))
    print("{} * {} = {}".format(3, vec, 3 * vec))

    print("+{} = {}".format(vec, +vec))
    print("-{} = {}".format(vec, -vec))

    zero2 = Vector.zero(2)
    print(zero2)
    print("{} + {} = {}".format(vec, zero2, vec + zero2))

    print("norm({}) = {}".format(vec, vec.norm()))
    print("norm({}) = {}".format(zero2, zero2.norm()))

    print("normalize{} is  {}".format(vec, vec.normalize()))
    print(vec.normalize().norm())  # 1

    try:
        zero2.normalize()
    except ZeroDivisionError:
        print("Cannot normalize zero vector {}.".format(zero2))

    print("{} dot product {} = {}".format(vec, vec2, vec.dot(vec2)))
    print()

    vec3 = Vector([0, 0])
    print("{} == {}? {}".format(zero2, vec3, zero2 == vec3))
    print("{} == {}? {}".format(vec2, vec3, vec2 == vec3))
    print("{} != {}? {}".format(vec2, vec3, vec2 != vec3))

