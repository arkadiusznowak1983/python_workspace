import unittest
from nondupcharacter import Nondupcharacter

class NondupcharacterTestCase(unittest.TestCase):
    def test_nondup(self):
        self.assertEqual((Nondupcharacter()).first('GeeksforGeeks'), 'f')
        self.assertEqual((Nondupcharacter()).first('GeeksQuiz'), 'G')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(NondupcharacterTestCase)
    unittest.TextTestRunner(verbosity=5).run(suite)
