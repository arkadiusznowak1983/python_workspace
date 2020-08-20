
def average(N=[]):
    result={}
    max=None
    for [student, grade] in N:
        result[student] = [result[student][0]+1, int((result[student][1]+int(grade))/(result[student][0]+1))] if student in result.keys() else [1, int(grade)]
        if (max is None) or (result[student][1] > max):
            max = result[student][1]
    return max
print(average([ ['Bobby', '65'], ['Charles', '22'], ['David', '-12'], ['Charles', '50'] ]))