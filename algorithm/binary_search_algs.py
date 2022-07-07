# Suppose you are given an array of size N in sorted order and you have to return the index of an element.
import math

class binary:
    def bin_search(self, N, search, min, max):
        if max < min:
            return -1
        mid = math.ceil((max+min)/2)
        if N[mid] == search:
            return mid
        if N[mid] > search:
            return self.bin_search(N, search, min, mid-1)
        else:
            return self.bin_search(N, search, mid, max)
    def search(self, N, search):
        return self.bin_search(N, search, 0, len(N)-1)
# N=[2,3,4,5,6,7,8,9]
# search=7
# print( binary().search(N, search) )
##################################################################################################################

class binary_linear:
    def search(self, N, search):
        left=0
        right=len(N)-1
        while(left<=right):
            mid = math.ceil((left+right)/2)
            if N[mid] < search:
                left = mid
            elif N[mid] > search:
                right = mid - 1
            else:
                return mid
        return -1
# N=[2,3,4,5,6,7,8,9]
# search=7
# print( binary_linear().search(N, search) )
##################################################################################################################


# Given a sorted array with repeating integers. You need to find the first occurence , last occurence and count of a given key in the array. USE ONLY BINARY SEARCH. Your algorithm should run in LogN time.If element is not present print -1 -1 0.
#
# looking: lower bound, upper bound, occurence
class bin_search:
    def search_left(self, N, search, left, right):
        mid=math.ceil((left+right)/2)
        if N[mid] < search:
            return self.search_left(N, search, mid, right)
        elif N[mid] > search:
            return self.search_left(N, search, left, mid-1)
        elif N[mid] == search:
            right=mid-1
            if left < right and mid > 0 and N[right] == search:
                return self.search_left(N, search, left, right)
            else:
                return mid

    def search_right(self, N, search, left, right):
        mid = math.ceil((left + right) / 2)
        if N[mid] < search:
            return self.search_right(N, search, mid, right)
        elif N[mid] > search:
            return self.search_right(N, search, left, mid-1)
        elif N[mid] == search:
            left = mid + 1
            if left < right and mid < len(N)-1 and N[left] == search:
                return self.search_right(N, search, left, right)
            else:
                return mid

    def search(self, N, search):
        if search > N[len(N)-1] or search < N[0]:
            return [ -1, -1, 0 ]

        left=self.search_left(N, search, 0, len(N)-1)
        right=self.search_right(N, search, 0, len(N)-1)

        return [ left, right, right-left+1 ]
# N=[1, 2, 2, 2, 3, 4]
# search=2
# print(bin_search().search(N, search))


# Find the minimum element in a sorted and rotated array
# A sorted array is rotated at some unknown point, find the minimum element in it.
# The following solution assumes that all elements are distinct.

class binary_rotated:
    def search_rot(self, N, low, height):
        if height < low:
            return N[0]

        if height == low:
            return N[low]

        mid = int((low+height)/2)

        if mid < height and N[mid+1] < N[mid]:
            return N[mid+1]

        if mid > low and N[mid] < N[mid-1]:
            return N[mid]

        if N[height] > N[mid]:
            return self.search_rot(N, low, mid-1)
        return self.search_rot(N, mid+1, height)

    def search(self, N):
        return self.search_rot(N, 0, len(N)-1)


N=[5, 6, 2, 3, 4]
print(binary_rotated().search(N))