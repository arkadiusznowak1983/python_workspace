#
Node = {'words': []}
map = {}
map["a"] = map["b"] = map["c"] = '2'
map["d"] = map["e"] = map["f"] = '3'
map["g"] = map["h"] = map["i"] = '4'
map["j"] = map["k"] = map["l"] = '5'
map["m"] = map["n"] = map["o"] = '6'
map["p"] = map["q"] = map["r"] = map["s"] = '7'
map["t"] = map["u"] = map["v"] = '8'
map["w"] = map["x"] = map["y"] = map["z"] = '9'

#
def add_character(tree, character):
    if character not in tree:
        tree[character] = Node.copy()
    return tree[character]

#
def add_word(tree, word):
    node = tree
    for character in word:
        node = add_character(tree=node, character=map[character])
    node['words'] = node['words'] + [word]

#
def create_tree(words):
    tree = Node.copy()
    if words is not None or len(words) == 0:
        for word in words:
            add_word(tree, word)
    return tree

#
def find_phone_number(tree, phone_number):
    for digit in phone_number:
        if digit not in tree:
            return []
        tree = tree[digit]
    return tree['words']

#
def phone_number_words(phone_number, words):
    tree = create_tree(words)
    return find_phone_number(tree=tree, phone_number=phone_number)

##
#
print("test 1: 366227: ", phone_number_words( phone_number='227', words=['bar', 'cap', 'car', 'emo', 'foo', 'foobar'] ))
assert phone_number_words( phone_number='227', words=['bar', 'cap', 'car', 'emo', 'foo', 'foobar'] ) == ['bar', 'cap', 'car']

print("test 1: 366227: ", phone_number_words( phone_number='2277', words=['bar', 'cap', 'car', 'emo', 'foo', 'foobar'] ))
assert phone_number_words( phone_number='2277', words=['bar', 'cap', 'car', 'emo', 'foo', 'foobar'] ) == []

assert phone_number_words( phone_number='365227', words=['bar', 'cap', 'car', 'emo', 'foo', 'foobar'] ) == []
print("test 1: 366227: ", phone_number_words( phone_number='365227', words=['bar', 'cap', 'car', 'emo', 'foo', 'foobar'] ))

assert phone_number_words( phone_number='366227', words=['bar', 'cap', 'car', 'emo', 'foo', 'foobar'] ) == ['foobar']
print("test 1: 366227: ", phone_number_words( phone_number='366227', words=['bar', 'cap', 'car', 'emo', 'foo', 'foobar'] ))