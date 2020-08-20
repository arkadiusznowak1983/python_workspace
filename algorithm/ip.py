def isIp(word):
    arr = word.split('.')
    if len(arr) != 4:
        return False
    for element in arr:
        if not (int(element) >= 0 and int(element) <= 255):
            return False
    return True

def chckip(text):
    arr=text.split(' ')
    mostCommon = None
    countArr = {}
    for word in arr:
        if isIp(word):
            countArr[word] = countArr[word]+1 if word in countArr.keys() else 1
            if mostCommon is None or countArr[word] > countArr[mostCommon]:
                mostCommon = word

    return mostCommon



print(chckip("zcz zc sdf fsdf sdf 123.123.123.124 dsfsdf sdf sdf" \
     "zcz zc sdf fsdf sdf 123.123.122.124 dsfsdf sdf sdf" \
     "zcz zc sdf fsdf sdf 123.123.122.124 dsfsdf sdf sdf" \
     "zcz zc sdf fsdf sdf 123.123.124.124 dsfsdf sdf sdf"))