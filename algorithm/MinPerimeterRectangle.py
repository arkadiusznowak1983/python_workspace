import math

def f(area):
    minPerimeter = None
    for i in range(1, int(math.sqrt(area)+1)):
        if area % i == 0 and (minPerimeter is None or minPerimeter > 2 * (i + area//i)):
            minPerimeter = 2 * (i + area // i)
    return minPerimeter

print(f(30))