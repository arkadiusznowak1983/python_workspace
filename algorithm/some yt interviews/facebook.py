'''
IS IT FINISHED ????

https://www.youtube.com/watch?v=psQ2lpH2hMQ
output:
0
1
00
01
10
11
000
001
...
infinite
'''
class interview_facebook:
    def printBinary(number, depth):
        buffer = ""
        if depth >= 3:
            return ""

        if number == 2:
            depth+=1
            return (__class__.printBinary(0, depth))

        if depth == 1:
            print( "{}".format( __class__.printBinary(number, depth)) )
            return str(number)
        else:
            return str(__class__.printBinary(number, depth))

        number+=1
        return str((__class__.printBinary(number, depth)))
