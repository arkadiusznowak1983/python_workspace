import unittest
from reverse_word import ReverseWord

class ReverseWordTestCase(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual( 'code practice quiz geeks'
                         , ReverseWord().getReversed('geeks quiz practice code'))
        self.assertEqual( 'practice of lot a needs coding at good getting'
                         , ReverseWord().getReversed('getting good at coding needs a lot of practice'))


if __name__ == '__main__':
    unittest.main()
