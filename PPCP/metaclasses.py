# class&object from type()
C = type('C', (), {'a': 111})
assert C.a == 111

c = C()
c.b = 1
assert c.b == 1

# create class with function as constructor
def magic_init(self):
    self.d = 1

C = type('C', (), {'__init__': magic_init})
assert C().d == 1

# creating own metaclass
class Meta(type):
    def __new__(mcs, *args, **kwargs):
        obj = super().__new__(mcs, *args, **kwargs)
        obj.a = "test"
        return obj
assert 'a' not in Meta.__dict__

class Object(metaclass=Meta):
    pass
assert Object.a == "test"

# add metaclass function and attr
del Meta
def meta_str(self):
    return f"{self.b}"

class Meta(type):
    def __new__(mcs, name, bases, dictionary):
        dictionary['__str__'] = meta_str
        dictionary['b'] = 1
        return super().__new__(mcs, name, bases, dictionary)

class Object(metaclass=Meta):
    pass

assert '__str__' in Object.__dict__
assert Object.b == 1
assert str(Object()) == "1"


