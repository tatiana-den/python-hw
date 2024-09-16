def polyEval(poly, x):
    hodnPol = 0
    for i in range(0, len(poly)):
        hodnPol += poly[i] * (x ** i)
    return hodnPol


def polySum(poly1, poly2):
    soucet = []
    if len(poly1) > len(poly2):
        delta = len(poly1) - len(poly2)
        for i in range(0, delta):
            poly2.append(0)
    elif len(poly1) < len(poly2):
        delta = len(poly2) - len(poly1)
        for i in range(0, delta):
            poly1.append(0)
    for i in range(0, len(poly1)):
        soucet.append(poly1[i] + poly2[i])
    soucet.reverse()
    while soucet[0] == 0:
        del soucet[0]
    soucet.reverse()
    return soucet


def polyMultiply(poly1, poly2):
    soucin = []
    delta = len(poly1) + len(poly2) - 1
    for i in range(0, delta):
        soucin.append(0)
    for i in range(0, len(poly1)):
        for j in range(0, len(poly2)):
            soucin[i + j] += poly1[i] * poly2[j]
    return soucin