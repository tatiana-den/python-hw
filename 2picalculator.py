import math


def newtonPi(init):
    x0 = init
    x1 = 0
    while x0 != x1:
        if x0 == float(x0 - ((math.sin(x0) / math.cos(x0)))):
            return x0
        else:
            x0 = float(x0 - ((math.sin(x0) / math.cos(x0))))


def leibnizPi(iterations):
    const = 4
    delta = 1
    pi = 0
    for i in range(0, iterations):
        if i % 2 == 0:
            pi += const / delta
        else:
            pi -= const / delta
        delta += 2
    return pi


def nilakanthaPi(iterations):
    const = 4
    delta = 2
    pi = 0
    for i in range(0, iterations):
        if i == 0:
            pi += 3
        else:
            if i % 2 == 0:
                pi -= const / (delta * (delta + 1) * (delta + 2))
            else:
                pi += const / (delta * (delta + 1) * (delta + 2))
            delta += 2
    return pi
