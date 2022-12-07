import string

CHARACTERS = str(list(string.ascii_letters) + [' '])


def letter_frequency(sentence):
    frequencies = [(c, 0) for c in CHARACTERS]
    for letter in sentence:
        index = CHARACTERS.index(letter)
        frequencies[index] = (letter, frequencies[index][1] + 1)
    return frequencies


class WeirdSortee:
    def __init__(self, number, string, sort_num):
        self.number = number
        self.string = string
        self.sort_num = sort_num

    def __lt__(self, object):
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string

    def __repr__(self):
        return "{} : {}".format(self.string, self.number)
