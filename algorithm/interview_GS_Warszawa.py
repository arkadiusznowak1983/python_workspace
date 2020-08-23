# Problem Name is &&& Snowpack &&& PLEASE DO NOT REMOVE THIS LINE.

def maxT(arr):
    if len(arr):
        maxE = arr[0]
        for elem in arr:
            if elem > maxE:
                maxE = elem
        return maxE
    return 0


def computeSnowpack(arr):
    arrL = []
    arrR = []
    sumArr = 0
    # maksLR = None
    for elem in range(len(arr)):
        arrL = arr[:elem]
        # print('l', arrL)
        arrR = arr[elem:]
        # print('r', arrR)
        maxL = maxT(arrL)
        maxR = maxT(arrR)
        maksLR = min(maxL, maxR)
        addVal = max(0, maksLR - arr[elem])
        # print('val', elem, addVal)
        sumArr = sumArr + addVal
    return sumArr


"""
 [[[0,1,3,0,1,2,0,4,2,0,3,0], 13]]
 maxL = 0
 maxR = 0

 arrL = 


 Instructions to candidate.
  1) Given an array of non-negative integers representing the elevations
     from the vertical cross section of a range of hills, determine how
     many units of snow could be captured between the hills. 

     See the example array and elevation map below.
                                 ___
             ___                |   |        ___
            |   |        ___    |   |___    |   |
         ___|   |    ___|   |   |   |   |   |   |
     ___|___|___|___|___|___|___|___|___|___|___|___
     [0,  1,  3,  0,  1,  2,  0,  4,  2,  0,  3,  0]
                                 ___
             ___                |   |        ___
            |   | *   *  _*_  * |   |_*_  * |   |
         ___|   | *  _*_|   | * |   |   | * |   |
     ___|___|___|_*_|___|___|_*_|___|___|_*_|___|___
     [0,  1,  3,  0,  1,  2,  0,  4,  2,  0,  3,  0]

     Solution: In this example 13 units of snow (*) could be captured.

  2) Consider adding some additional tests in doTestsPass().
  3) Implement computeSnowpack() correctly.
"""


def doTestsPass():
    """ Returns True if all tests pass. Otherwise returns False. """
    tests = [[[0, 1, 3, 0, 1, 2, 0, 4, 2, 0, 3, 0], 13],
             [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 10],
             [[0, 0, 0, 0, 0], 0],
             [[0, 0, 1, 0, 0], 0],
             [[1], 0],
             [[], 0]]

    for test in tests:
        if not (computeSnowpack(test[0]) == test[1]):
            return False
    return True


if __name__ == "__main__":
    if (doTestsPass()):
        print("All tests pass")
    else:
        print("Not all tests pass")
