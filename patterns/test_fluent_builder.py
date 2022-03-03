import unittest
from fluent_builder import FluentBuilder, Builder

class FluentBuilderTestCase(unittest.TestCase):
    def test_builderPassedToConstructor(self):
        builder = Builder()
        builder.attr1 = 'test_builderPassedToConstructor_attr1'
        builder.attr2 = 'test_builderPassedToConstructor_attr2'
        director = FluentBuilder(builder)
        print("new director -> {}".format(director))
        self.assertEqual( "{} {}".format('test_builderPassedToConstructor_attr1', 'test_builderPassedToConstructor_attr2')
                         ,"{}".format(director))
    def test_builderPassedToSetter(self):
        builder = Builder()
        builder.attr1 = 'test_builderPassedToSetter_attr1'
        builder.attr2 = 'test_builderPassedToSetter_attr2'
        director = FluentBuilder()
        director.builder = builder
        print("new director -> {}".format(director))
        self.assertEqual( "{} {}".format('test_builderPassedToSetter_attr1', 'test_builderPassedToSetter_attr2')
                         ,"{}".format(director))

if __name__ == '__main__':
    unittest.main()
