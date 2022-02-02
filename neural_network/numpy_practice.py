import numpy as np
import math


def main():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = 10


    a = np.array(a)
    b = np.array(b)

    # element-wise addition
    # vector + scalar
    add_1 = np.add(a, c)
    plus_1 = a + c
    print(f"np.add: {add_1}")
    print(f"a + c: {plus_1}")

    
    # vector + vector
    add_2 = np.add(a, b)
    print(add_2)
    print(a + b)

    # vector * scalar
    mul_1 = np.multiply(a, c)
    print(mul_1)
    print(a * c)

    # vector * vector
    mul_2 = np.multiply(a, b)
    print(mul_2)
    print(a * b)

    # cuztom func
    f = lambda x : 1 / (1 + math.exp(-x))
    custom = f(a)
    print(custom)

if __name__ == "__main__":
    main()
