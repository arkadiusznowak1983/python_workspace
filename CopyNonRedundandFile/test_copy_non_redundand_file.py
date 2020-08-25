import unittest
from CopyNonRedundandFile import CopyNonRedundandFile


class CopyNonRedundandFileTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, CopyNonRedundandFile().copy( existing_path="R:\\folder2"
                                                           ,new_path="R:\\folder1"
                                                           ,destination_path="R:\\folder3"))


if __name__ == '__main__':
    unittest.main()
