import unittest
from egsfloor import Egsfloor

class EgsfloorTestCase(unittest.TestCase):
    def test_minim(self):
        self.assertEqual(3, Egsfloor().eggDrop( eggs=2, floors=10, operation=min))
        self.assertEqual(36, Egsfloor().eggDrop(eggs=1, floors=36, operation=min))
        self.assertEqual(7, Egsfloor().eggDrop(eggs=2, floors=36, operation=min))

    def test_max(self):
        self.assertEqual(3, Egsfloor().eggDrop( eggs=2, floors=10, operation=max))
        self.assertEqual(36, Egsfloor().eggDrop(eggs=1, floors=36, operation=max))
        self.assertEqual(9, Egsfloor().eggDrop(eggs=2, floors=36, operation=max))
