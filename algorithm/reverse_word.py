class ReverseWord:
    '''
    https://www.geeksforgeeks.org/reverse-words-in-a-given-string/

    Example: Let the input string be “i like this program very much”. The function should change the string to “much very program this like i”

        Input: s = “geeks quiz practice code”
        Output: s = “code practice quiz geeks”

        Input: s = “getting good at coding needs a lot of practice”
        Output: s = “practice of lot a needs coding at good getting”

        time complexity: O(n)
        space complexity: O(n)  ???
    '''
    def getReversed(self, word):
        tmpWord = ''
        words = []
        for letter in word + ' ':
            if letter == ' ' and len(tmpWord) > 0:
                words.append(tmpWord)
                tmpWord = ''
            else:
                tmpWord = tmpWord + letter
        return " ".join(words[::-1])