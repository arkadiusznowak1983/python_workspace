
class SortMerge:
    '''
    https://www.geeksforgeeks.org/merge-sort/

    Like QuickSort, Merge Sort is a Divide and Conquer algorithm.
    It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.
    The merge() function is used for merging two halves.
    The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.
    See following C implementation for details.

    MergeSort(arr[], l,  r)
    If r > l
         1. Find the middle point to divide the array into two halves:
                 middle m = (l+r)/2
         2. Call mergeSort for first half:
                 Call mergeSort(arr, l, m)
         3. Call mergeSort for second half:
                 Call mergeSort(arr, m+1, r)
         4. Merge the two halves sorted in step 2 and 3:
                 Call merge(arr, l, m, r)
    '''

    def sort_own(self, arr=[]):
        '''
        time complexity: O(n*log(n))
        space complexity: O(n)
        '''
        if len(arr) <= 1:
            return arr

        half = len(arr) // 2
        arr_l = self.sort_own(arr[:half])
        arr_r = self.sort_own(arr[half:])

        indeks_l = indeks_r = indeks_arr = 0
        while(indeks_l < len(arr_l) and indeks_r < len(arr_r)):
            if arr_l[indeks_l] < arr_r[indeks_r]:
                arr[indeks_arr] = arr_l[indeks_l]
                indeks_l = indeks_l + 1
            else:
                arr[indeks_arr] = arr_r[indeks_r]
                indeks_r = indeks_r + 1
            indeks_arr = indeks_arr + 1

        while(indeks_l < len(arr_l)):
            arr[indeks_arr] = arr_l[indeks_l]
            indeks_l = indeks_l + 1
            indeks_arr = indeks_arr + 1
        while (indeks_r < len(arr_r)):
            arr[indeks_arr] = arr_r[indeks_r]
            indeks_r = indeks_r + 1
            indeks_arr = indeks_arr + 1

        return arr

    def merge_sort(self, arr=[]):
        if len(arr) <= 1:
            return arr

        half = len(arr) // 2
        left = arr[:half]
        right = arr[half:]
        left = self.merge_sort(left)    # recursion
        right = self.merge_sort(right)  # recursion

        arr = []
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                arr.append(left.pop(0))
            else:
                arr.append(right.pop(0))

        [arr.append(i) for i in left]
        [arr.append(i) for i in right]

        return arr
