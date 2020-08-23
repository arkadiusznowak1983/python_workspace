# https://www.geeksforgeeks.org/minimize-the-maximum-difference-between-the-heights/
#
# i'am not sure that solution, check it before use
#
class DifferenceBetweenHeights:
    '''
    Given heights of n towers and a value k.
    We need to either increase or decrease height of every tower by k (only once) where k > 0.
    The task is to minimize the difference between the heights of the longest and the shortest tower after modifications,
    and output this difference.

    Input  : arr[] = {1, 15, 10}, k = 6
    Output :  Maximum difference is 5.
    Explanation : We change 1 to 6, 15 to
    9 and 10 to 4. Maximum difference is 5
    (between 4 and 9). We can't get a lower
    difference.

    Input : arr[] = {1, 5, 15, 10}
            k = 3
    Output : Maximum difference is 8
    arr[] = {4, 8, 12, 7}
    '''
    def calc(self, arr, k):
        arr.sort()
        diff = arr[-1] - arr[0]
        small = arr[0] + k
        big = arr[-1] - k
        if small > big:
            small, big = big, small
        for i in range(1,len(arr)-1):
            subtract = arr[i] - k
            add = arr[i] + k
            if (subtract >= small or add <= big):
                continue
            if (big - subtract <= add - small):
                small = subtract
            else:
                big = add
        return min(diff, big-small)