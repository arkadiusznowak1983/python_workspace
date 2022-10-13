def closure_default_example():
    # default example of closure
    def outer(attribute):
        attributes = [attribute]

        def inner():
            return attributes
        return inner

    def another_function(param):
        print(param())

    if __name__ == "__main__":
        closure = outer('Test value')
        another_function(closure)


def closure_list():
    def store(attribute):
        attributes = [attribute]

        def add(param):
            nonlocal attributes
            attributes.append(param)

        def get(index=None):
            return attributes if index is None else attributes[index]
        return add, get

    def test(add, get):
        print('all', get())
        print('0', get(0))
        add('second element')
        print('all', get())

    if __name__ == "__main__":
        add, get = store('Test value 1')
        test(add, get)


if __name__ == "__main__":
    closure_list()