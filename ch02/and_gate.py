import numpy as np

weight = [0.5,0.5]
bias = 0.4

def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([weight[0],weight[1]])
    b = -bias
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    for xs in [(0,0),(1,0),(0,1),(1,1)]:
        y = AND(xs[0],xs[1])
        print(str(xs)+" -> "+str(y))