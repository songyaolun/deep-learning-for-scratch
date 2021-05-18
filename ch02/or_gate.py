import numpy as np

weight = [0.5,0.5]
bias = 0.2

def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([weight[0],weight[1]])
    b = -bias
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    for xs in [(0,0),(1, 0), (0, 1), (1, 1)]:
        y = OR(xs[0],xs[1])
        print(str(xs) + " -> " + str(y))