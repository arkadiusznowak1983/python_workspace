import unittest
from facebook import interview_facebook

class TestRun(unittest.TestCase):
    def test_run(self):
        pass #elf.assertEqual((interview_facebook()).printBinary(0,1), True)


if __name__ == '__main__':
    pass
    #suite = unittest.TestLoader().loadTestsFromTestCase(TestRun)
    #suite = unittest.TestLoader().loadTestsFromName( 'test_binary', SearchArrayTestCase )
    #unittest.TextTestRunner(verbosity=2).run(suite)

# t =  [x if x % 2 == 0 else [a for a in [9,8,7]] for x in [2,3,4,5]]
buffer=str() # rint(buffer) for depth in [buffer.__add__(str(number))
#def f():
#    return [ number if number in [0,1] else f() for number in [0,1]]]

# numery = lambda x: (x + 1) % 2



def f(level=0, arr=[]):
    for numer in [0, 1]:
        for waiter in range(int(pow(2, level))):
            tab = arr.copy()
            tab.append(numer)
            tab.append(numer)
    return tab
print( f(0), [1,1] )


#print([0]+[1])
#
# buffer=str()
# depth=5
# print([[numer, level] for numer in [0,1] for level in [0,1]])



# kk=20
# if (kk+=1)== 20:
#     print(kk)
#     print(++kk)
#     print(kk)