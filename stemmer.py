# Implementation of the Porter Stemmer algorithm defined at:
# https://tartarus.org/martin/PorterStemmer/def.txt

class Stemmer:
    def __init__(self):
        self.vowels = {'a', 'e', 'i', 'o', 'u'}
        self.consonants = {'z', 'v', 'x', 'm', 'l', 'f', 's', 'b', 'd', 'w', 'h', 'r', 'g', 'q', 'n', 'j', 'c', 't', 'k', 'p'}
        # not including 'y' because it is sometimes one or the other

    # breaks word into the format [C](VC)^m[V]
    def atomize(self):
        # TODO: implement
        m = 0
        head = 0
        tail = 0
        return m

    def __replace(self, word, suffix, replacement):
        return word[ : len(word) - len(suffix)] + replacement

    # TODO: implement all star helper funcs
    # checks if the stem of word contains a vowel
    def __v_star(self, word, suffix):
        return True

    # checks if the word ends with a double consonant
    def __d_star(self, word):
        return True

    def __o_star(self, word):
        return True

    def stem(self, word):
        m = self.atomize(word)

        # step 1a
        if word.endswith('sses'):
            word = self.__replace(word, 'sses', 'ss')
        elif word.endswith('ies'):
            word = self.__replace(word, 'ies', 'i')
        elif word.endswith('ss'):
            word = self.__replace(word, 'ss', 'ss')
        elif word.endswith('s'):
            word = self.__replace(word, 's', '')

        # step 1b
        restore_e = False
        if word.endswith('eed') and m > 0:
            word = self.__replace(word, 'eed', 'ee')
        elif word.endswith('ed') and self.__v_star(word, 'ed'):
            word = self.__replace(word, 'ed', '')
            restore_e = True # TODO: rename this variable
        elif word.endswith('ing') and self.__v_star(word, 'ing'):
            word = self.__replace(word, 'ing', '')
            restore_e = True

        if restore_e:
            if word.endswith('at'):
                word = word + 'e'
            elif word.endswith('bl'):
                word = word + 'e'
            elif word.endswith('iz'):
                word = word + 'e'
            elif self.__d_star(word) and not (word.endswith('l') or word.endswith('s') or word.endswith('z')):
                word = word[ : len(word) - 1]
            elif m == 1 and self.__o_star(word):
                word = word + 'e'

        # step 1c
        if word.endswith('y') and self.__v_star(word, 'y'):
            word = self.__replace(word, 'y', 'i')
