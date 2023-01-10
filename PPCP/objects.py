from copy import copy, deepcopy
from pickle import dump, dumps, load, loads
from pytest import raises
import shelve


class C:
    def __init__(self):
        self.p = "".join([chr(x) for x in range(65, 65 + 32 + 30)])

    def __str__(self):
        return self.p

    def __eq__(self, other):
        return self.p == other.p


print("aaaa.bbbbb.cccc".split(" ")[0])
obj = C()
print('obj.p => ', obj.p)

# shallow copy
obj_copy = copy(obj)
print(obj is obj_copy, obj == obj_copy)
print('ids => ', id(obj), id(obj_copy))

# deep copy
obj_deepcopy = deepcopy(obj)
print(obj is obj_deepcopy, obj == obj_deepcopy)
print('ids => ', id(obj), id(obj_deepcopy))

# serialization
obj_serialized = dumps(obj)
print(f"obj.p => {obj.p}")
print(f"serialization => {obj_serialized}")
with open(f"tmp/obj_instance_serialized.dat", "wb") as file:
    dump(obj, file)

# deserialization
print(f"deserialization => {loads(obj_serialized)}")
with open(f"tmp/obj_instance_serialized.dat", "rb") as file:
    obj_deserialized = load(file)
print(f"deserialized => {obj_deserialized}")
assert obj.p == obj_deserialized.p
assert obj == obj_deserialized

print(f"None serialized=> {dumps(None)}")
assert loads(dumps(None)) is None

# serialize&deserialize function
def f(x):
    return 2*x if x else 1
assert loads(dumps(f))('a') == f('a')

deserialized_f = loads(dumps(f))
def f2(x):
    return 5*x if x else 0
f = f2
assert deserialized_f('a') != f('a')

#  deserialize deleted function
def f_to_delete():
    print('test f_to_delete function')

with open("tmp/f_to_delete.pckl", 'wb') as file:
    dump(f_to_delete, file)

del f_to_delete
with open("tmp/f_to_delete.pckl", 'rb') as file:
    with raises(AttributeError):
        load(file)

#  deserialize deleted class object
with open("tmp/C_class.pckl", 'wb') as file:
    dump(C(), file)

del C
with open("tmp/C_class.pckl", 'rb') as file:
    with raises(AttributeError):
        load(file)

# shelve
name = 'shelve db'
with shelve.open(name, 'n') as shl:
    shl['test-key'] = 'test value'

with shelve.open(name) as shl:
    assert 'test-key' in shl and shl['test-key'] == 'test value', [x for x in shl.keys()]


