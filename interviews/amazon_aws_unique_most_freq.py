# solution for online technica interview AMazon AWS
# https://www.youtube.com/watch?v=t0OQAD5gjd8
################################################
import unittest
import collections

# solutions
#################################################

# solution 1
def calc_using_collections(nums,uniqsCount):
    assert len(nums) >= 1, "Pusta lista nums"
    assert uniqsCount >= 1, "Liczba k mniejsza niż 1"

    return [v for k,v in enumerate(collections.Counter(nums)) if k < uniqsCount]

# solution 2
def calc_two_arrays(nums,uniqsCount):
    assert len(nums) >= 1, "Pusta lista nums"
    assert uniqsCount >= 1, "Liczba k mniejsza niż 1"

    uniqList = []
    doublesList = []
    doubles = 0
    value = None
    for k,v in enumerate(sorted(nums)):
        doubles += 1
        if value != v or k == len(nums)-1:
            uniqList.append(v if value == None else value)
            doublesList.append(doubles)
            value = v
            doubles = 0
        if value == None:
            value = v
            doubles = 0

    return [uniqList[i[0]] for index,i in enumerate(sorted({k:v for k,v in enumerate(doublesList)}.items(), key = lambda item:item[1], reverse=True)) if index < uniqsCount or index == 1]

# tests
######################################################
# solution 1
def test__calc_collections():
    assert calc_using_collections([1,1,1,2,2,3],2) == [1,2], "test__calc_collections: Niespelniono dla nums:[1,1,1,2,2,3] k:2"
def test__calc_collections2():
    assert calc_using_collections([1],1) == [1], "test__calc_collections: Niespelniono dla nums:[1] k:1"

# solution 2
def test__calc_two_arrays():
    assert calc_two_arrays([1,1,1,2,2,3],2) == [1,2], "test__calc_collections: Niespelniono dla nums:[1,1,1,2,2,3] k:2"
def test__calc_two_arrays2():
    assert calc_two_arrays([1],1) == [1], "test__calc_collections: Niespelniono dla nums:[1] k:1"



test__calc_collections()
test__calc_collections2()
test__calc_two_arrays()
test__calc_two_arrays2()