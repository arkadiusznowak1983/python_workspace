from observer_pattern import ObserverNameException
import unittest

def myF():
    raise Exception('exp_test_1')

class MyTestCase(unittest.TestCase):
    def test_exception(self):
        try:
            myF()
        except ObserverNameException:
            print('except ObserverNameException')
            return
        except:
            pass
        self.fail('ObserverNameException not apperas')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    unittest.TextTestRunner(verbosity=0).run(suite)