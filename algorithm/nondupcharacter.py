# https://www.geeksforgeeks.org/given-a-string-find-its-first-non-repeating-character/
class Nondupcharacter:
    def first(self, word):
        arr={}
        for char in word:
            if char in arr.keys():
                arr[char] = arr[char] + 1
            else:
                arr[char] = 1

        for k,v in arr.items():
            if v == 1:
                return k
        return ''
