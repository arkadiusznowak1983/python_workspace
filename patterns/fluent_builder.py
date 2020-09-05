class Builder():
    def __init__(self):
        self.reset()

    @property
    def attr1(self):
        pass
    @attr1.getter
    def attr1(self):
        return self._attr1
    @attr1.setter
    def attr1(self, val):
        self._attr1 = val
    @property
    def attr2(self):
        pass
    @attr2.getter
    def attr2(self):
        return self._attr2
    @attr2.setter
    def attr2(self, val):
        self._attr2 = val
        if 'attr2' not in self.params:
            self.params.append('attr2')
    def reset(self):
        self._attr1 = str('')
        self.params = ['attr1']
    def __repr__(self):
        if len(self.params) == 0:
            return ''
        result = ''
        for element in self.params:
            result = result + getattr(self, element) + ' '
        return result[:-1]


class FluentBuilder:
    def __init__(self, builder=None):
        self._builder = builder
    @property
    def builder(self):
        pass
    @builder.getter
    def builder(self):
        return self._builder
    @builder.setter
    def builder(self, val):
        self._builder = val

    def __repr__(self):
        return str(self._builder)

if __name__ == "__main__":
    pass
#     director = FluentBuilder()
#     builder = Builder()
#     director.builder = builder
#     print("director -> {}".format(director))
#     builder.attr1 = str('value 1')
#     print("director changed attr1 -> {}".format(director))
#     builder.attr2 = str('value 2')
#     print("director with sttr2 -> {}".format(director))
#     print("director.builder.attr2 -> {}".format(director.builder.attr2))
#
#     builder = Builder()
#     builder.attr1 = 'test_attr1'
#     builder.attr2 = 'test_attr2'
#     director = FluentBuilder(builder)
#     print("new director -> {}".format(director))