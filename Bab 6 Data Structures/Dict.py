randomKey = {}
randomKey["string"] = 'bisa naro string'
randomKey['5'] = 'ini integer'
randomKey['25.42'] = 'bisa juga naro flaot'
randomKey['abc', 5] = 'bahkan bisa naro dict yang laen'


class AnObject:
    def __init__(self, avelue):
        self.avelue = avelue


my_object = AnObject(14)
randomKey[my_object] = 'kita dapat naro object'
my_object.avelue = 12

try:
    my_object[[1, 2, 3]] = 'tidak bisa naro list'
except:
    print("Unable to add list\n")

for key, value in randomKey.items():
    print("{} bernilai {}".format(key, value))

from collections import defaultdict


def letter_frequence(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies


num_items = 0


def tupple_counter():
    global num_items
    num_items += 1
    return num_items, []


d = defaultdict(tupple_counter)

