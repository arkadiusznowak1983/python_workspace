# Merge and sort two sorted lists

def merge(first_arr, second_arr):
    index_first, index_second = 0, 0

    while index_first < len(first_arr) and index_second < len(second_arr):
        if first_arr[index_first] <= second_arr[index_second]:
            yield first_arr[index_first]
            index_first += 1
        else:
            yield second_arr[index_second]
            index_second += 1

    for element in first_arr[index_first:] + second_arr[index_second:]:
        yield element


first_arr = [1, 3, 5, 8]
second_arr = [1, 2, 4]
expected = [1, 1, 2, 3, 4, 5, 8]

print("Test ", first_arr, second_arr, 'result', expected)
assert merge(first_arr, second_arr), expected
