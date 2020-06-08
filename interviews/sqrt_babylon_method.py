import unittest

debug = True

# babylonian method square root
def calc_sqrt(S):
    print("# S: " + str(S)) if debug else None
    # calc n for S0 = a * 10^n, a in 2,6
    stringS = str(S)
    if (len(stringS) % 2) == 1:
        n = (len(stringS)-1) / 2
        xn = 2 * (10 ** n)
    else:
        n = (len(stringS) - 2) / 2 # a = 6
        xn = 6 * (10 ** n)

    # calculate Xn+1 = (1 /2) * (Xn + (S / Xn))
    xn1 = 0
    while(xn1 != xn):
        xn = xn1 if xn1 != 0 else xn
        xn1 = (1 / 2) * (xn + (S / xn))
        print("Xn: " + str(xn) + ", Xn+1: " + str(xn1)) if debug else None

    return xn

# tests for babylonian method square root
def test_calc_sqrt():
    assert calc_sqrt(9) == 3
    assert calc_sqrt(15876) == 126
    assert calc_sqrt(125348) == 354.04519485512014

test_calc_sqrt()