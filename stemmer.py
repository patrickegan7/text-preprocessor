# Implementation of the Porter Stemmer algorithm defined at:
# https://tartarus.org/martin/PorterStemmer/def.txt

class Stemmer:
    def __init__(self):
        self.vowels = {'a', 'e', 'i', 'o', 'u'}
        self.consonants = {'z', 'v', 'x', 'm', 'l', 'f', 's', 'b', 'd', 'w', 'h', 'r', 'g', 'q', 'n', 'j', 'c', 't', 'k', 'p'}
        # not including 'y' because it is sometimes one or the other

    # breaks word into the format [C](VC)^m[V]
    def measure(self, word): # TODO: implement
        m = 0
        if len(word) <= 1:
            return m

        # handle when y is the starting letter
        start_core = 0
        if word[start_core] == 'y':
            start_core = 1

        # find the index where the (VC)^m starts
        in_prefix = True
        while in_prefix:
            if start_core < len(word) and word[start_core] in self.consonants:
                start_core += 1
            else:
                in_prefix = False

        # if y is the last letter determine if it is a vowel or a consonant
        end_core = len(word) - 1
        if word[end_core] == 'y' and word[end_core - 1] in self.consonants:
            end_core -= 1

        # find the index where the (VC)^m ends
        in_suffix = True
        while in_suffix:
            if end_core > -1 and word[end_core] in self.vowels:
                end_core -= 1
            else:
                in_suffix = False

        # m = 0
        if end_core < start_core:
            return m

        # find the value of m
        core = word[start_core : end_core + 1]
        idx = 0
        while idx < len(core):
            if core[idx] in self.consonants:
                m += 1
                idx += 1
                while idx < len(core) and core[idx] in self.consonants:
                    idx += 1
            else:
                idx += 1

        return m

    def __replace(self, word, suffix, replacement):
        return word[ : len(word) - len(suffix)] + replacement

    # checks if the stem of word contains a vowel
    def __v_star(self, word, suffix):
        stem = word[ : len(word) - len(suffx)]

        # handle case where 'y' is a vowel
        if 'y' in stem:
            i = stem.indexof('y')
            if i != 0 and stem[i - 1] in self.consonants:
                return True

        for char in stem:
            if char in self.vowels:
                return True

        return False

    # checks if the stem ends with a double consonant
    def __d_star(self, word, suffix):
        stem = word[ : len(word) - len(suffx)]

        if len(stem > 1):
            return stem[len(stem) - 1] in self.consonants and stem[len(stem) - 1] == stem[len(stem) - 2]
        return False

    # checks if the stem ends in cvc
    def __o_star(self, word, suffix):
        stem = word[ : len(word) - len(suffx)]

        if len(stem >= 3):
            if stem[len(stem) - 3] in self.consonants and (stem[len(stem) - 2] in self.vowels or  stem[len(stem) - 2] == 'y') and stem[len(stem) - 1] in self.consonants:
                return True
        return False

    def stem(self, word):
        m = self.measure(word)

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
            restore_e = True
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
            elif self.__d_star(word, '') and not (word.endswith('l') or word.endswith('s') or word.endswith('z')):
                word = word[ : len(word) - 1]
            elif m == 1 and self.__o_star(word, ''):
                word = word + 'e'

        # step 1c
        if word.endswith('y') and self.__v_star(word, 'y'):
            word = self.__replace(word, 'y', 'i')

        # step 2
        if word.endswith('ational') and m > 0:
            word = self.__replace(word, 'ational', 'ate')
        elif word.endswith('tional') and m > 0:
            word = self.__replace(word, 'tional', 'tion')
        elif word.endswith('enci') and m > 0:
            word = self.__replace(word, 'enci', 'ence')
        elif word.endswith('anci') and m > 0:
            word = self.__replace(word, 'anci', 'ance')
        elif word.endswith('izer') and m > 0:
            word = self.__replace(word, 'izer', 'ize')
        elif word.endswith('abli') and m > 0:
            word = self.__replace(word, 'abli', 'able')
        elif word.endswith('alli') and m > 0:
            word = self.__replace(word, 'alli', 'al')
        elif word.endswith('entli') and m > 0:
            word = self.__replace(word, 'entli', 'ent')
        elif word.endswith('eli') and m > 0:
            word = self.__replace(word, 'eli', 'e')
        elif word.endswith('ousli') and m > 0:
            word = self.__replace(word, 'ousli', 'ous')
        elif word.endswith('ization') and m > 0:
            word = self.__replace(word, 'ization', 'ize')
        elif word.endswith('ation') and m > 0:
            word = self.__replace(word, 'ation', 'ate')
        elif word.endswith('ator') and m > 0:
            word = self.__replace(word, 'ator', 'ate')
        elif word.endswith('alism') and m > 0:
            word = self.__replace(word, 'alism', 'al')
        elif word.endswith('iveness') and m > 0:
            word = self.__replace(word, 'iveness', 'ive')
        elif word.endswith('fulness') and m > 0:
            word = self.__replace(word, 'fulness', 'ful')
        elif word.endswith('ousness') and m > 0:
            word = self.__replace(word, 'ousness', 'ous')
        elif word.endswith('aliti') and m > 0:
            word = self.__replace(word, 'aliti', 'al')
        elif word.endswith('iviti') and m > 0:
            word = self.__replace(word, 'iviti', 'ive')
        elif word.endswith('biliti') and m > 0:
            word = self.__replace(word, 'biliti', 'ble')

        # step 3
        if word.endswith('icate') and m > 0:
            word = self.__replace(word, 'icate', 'ic')
        elif word.endswith('ative') and m > 0:
            word = self.__replace(word, 'ative', '')
        elif word.endswith('alize') and m > 0:
            word = self.__replace(word, 'alize', 'al')
        elif word.endswith('iciti') and m > 0:
            word = self.__replace(word, 'iciti', 'ic')
        elif word.endswith('ical') and m > 0:
            word = self.__replace(word, 'ical', 'ic')
        elif word.endswith('ful') and m > 0:
            word = self.__replace(word, 'ful', '')
        elif word.endswith('ness') and m > 0:
            word = self.__replace(word, 'ness', '')

        # step 4
        if word.endswith('al') and m > 1:
            word = self.__replace(word, 'al', '')
        elif word.endswith('ance') and m > 1:
            word = self.__replace(word, 'ance', '')
        elif word.endswith('ence') and m > 1:
            word = self.__replace(word, 'ence', '')
        elif word.endswith('er') and m > 1:
            word = self.__replace(word, 'er', '')
        elif word.endswith('ic') and m > 1:
            word = self.__replace(word, 'ic', '')
        elif word.endswith('able') and m > 1:
            word = self.__replace(word, 'able', '')
        elif word.endswith('ible') and m > 1:
            word = self.__replace(word, 'ible', '')
        elif word.endswith('ant') and m > 1:
            word = self.__replace(word, 'ant', '')
        elif word.endswith('ement') and m > 1:
            word = self.__replace(word, 'ement', '')
        elif word.endswith('ment') and m > 1:
            word = self.__replace(word, 'ment', '')
        elif word.endswith('ent') and m > 1:
            word = self.__replace(word, 'ent', '')
        elif word.endswith('ion') and m > 1:
            if len(word) > 3 and (word[ : len(word) - 3] == 's' or word[ : len(word) - 3] == 't'):
                word = self.__replace(word, 'ion', '')
        elif word.endswith('ou') and m > 1:
            word = self.__replace(word, 'ou', '')
        elif word.endswith('ism') and m > 1:
            word = self.__replace(word, 'ism', '')
        elif word.endswith('ate') and m > 1:
            word = self.__replace(word, 'ate', '')
        elif word.endswith('iti') and m > 1:
            word = self.__replace(word, 'iti', '')
        elif word.endswith('ous') and m > 1:
            word = self.__replace(word, 'ous', '')
        elif word.endswith('ive') and m > 1:
            word = self.__replace(word, 'ive', '')
        elif word.endswith('ize') and m > 1:
            word = self.__replace(word, 'ize', '')

        # step 5a
        if word.endswith('e') and m > 1:
            word = self.__replace(word, 'e', '')
        elif word.endswith('e') and m == 1 and not self.__o_star(word, 'e'):
            word = self.__replace(word, 'e', '')

        # step 5b
        if m > 1 and self.__d_star(word, '') and word.endswith('l'):
            word = word[ : len(word) - 1]

        return word
