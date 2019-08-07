# Implementation of the Porter Stemmer algorithm defined at:
# https://tartarus.org/martin/PorterStemmer/def.txt


# TODO: need to make all the conditions only apply to the stem, including conditions on a word's measure

class Stemmer:
    def __init__(self):
        self.vowels = {'a', 'e', 'i', 'o', 'u'}
        self.consonants = {'z', 'v', 'x', 'm', 'l', 'f', 's', 'b', 'd', 'w', 'h', 'r', 'g', 'q', 'n', 'j', 'c', 't', 'k', 'p'}
        # not including 'y' because it is sometimes one or the other

    # breaks word into the format [C](VC)^m[V]
    def measure(self, word):
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
        return self.__core(word, suffix) + replacement

    # checks if the stem of word contains a vowel
    def __v_star(self, word, suffix):
        stem = self.__core(word, suffix)

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
        stem = self.__core(word, suffix)

        if len(stem) > 1:
            return stem[len(stem) - 1] in self.consonants and stem[len(stem) - 1] == stem[len(stem) - 2]
        return False

    # checks if the stem ends in cvc
    def __o_star(self, word, suffix):
        stem = self.__core(word, suffix)

        if len(stem) >= 3:
            if stem[len(stem) - 3] in self.consonants and (stem[len(stem) - 2] in self.vowels or  stem[len(stem) - 2] == 'y') and stem[len(stem) - 1] in self.consonants:
                return True
        return False

    def __core(self, word, suffix):
        return word[ : len(word) - len(suffix)]

    def step_1a(self, word, m):
        if word.endswith('sses'):
            word = self.__replace(word, 'sses', 'ss')
        elif word.endswith('ies'):
            word = self.__replace(word, 'ies', 'i')
        elif word.endswith('ss'):
            word = self.__replace(word, 'ss', 'ss')
        elif word.endswith('s'):
            word = self.__replace(word, 's', '')

        return word

    def step_1b(self, word, m):
        restore_e = False
        if word.endswith('eed'):
            if self.measure(self.__core(word, 'eed')) > 0:
                word = self.__replace(word, 'eed', 'ee')
        elif word.endswith('ed'):
            if self.__v_star(word, 'ed'):
                word = self.__replace(word, 'ed', '')
                restore_e = True
        elif word.endswith('ing'):
            if self.__v_star(word, 'ing'):
                word = self.__replace(word, 'ing', '')
                restore_e = True

        if restore_e:
            if word.endswith('at'):
                word = word + 'e'
            elif word.endswith('bl'):
                word = word + 'e'
            elif word.endswith('iz'):
                word = word + 'e'
            elif self.__d_star(word, ''):
                if not (word.endswith('l') or word.endswith('s') or word.endswith('z')):
                    word = word[ : len(word) - 1]
            elif m == 1 and self.__o_star(word, ''):
                word = word + 'e'

        return word

    def step_1c(self, word, m):
        if word.endswith('y') and self.__v_star(word, 'y'):
            word = self.__replace(word, 'y', 'i')

        return word

    def step_2(self, word, m):
        if word.endswith('ational'):
            if self.measure(self.__core(word, 'ational')) > 0:
                word = self.__replace(word, 'ational', 'ate')
        elif word.endswith('tional'):
            if self.measure(self.__core(word, 'tional')) > 0:
                word = self.__replace(word, 'tional', 'tion')
        elif word.endswith('enci'):
            if self.measure(self.__core(word, 'enci')) > 0:
                word = self.__replace(word, 'enci', 'ence')
        elif word.endswith('anci'):
            if self.measure(self.__core(word, 'anci')) > 0:
                word = self.__replace(word, 'anci', 'ance')
        elif word.endswith('izer'):
            if self.measure(self.__core(word, 'izer')) > 0:
                word = self.__replace(word, 'izer', 'ize')
        elif word.endswith('abli'):
            if self.measure(self.__core(word, 'abli')) > 0:
                word = self.__replace(word, 'abli', 'able')
        elif word.endswith('alli'):
            if self.measure(self.__core(word, 'alli')) > 0:
                word = self.__replace(word, 'alli', 'al')
        elif word.endswith('entli'):
            if self.measure(self.__core(word, 'entli')) > 0:
                word = self.__replace(word, 'entli', 'ent')
        elif word.endswith('eli'):
            if self.measure(self.__core(word, 'eli')) > 0:
                word = self.__replace(word, 'eli', 'e')
        elif word.endswith('ousli'):
            if self.measure(self.__core(word, 'ousli')) > 0:
                word = self.__replace(word, 'ousli', 'ous')
        elif word.endswith('ization'):
            if self.measure(self.__core(word, 'ization')) > 0:
                word = self.__replace(word, 'ization', 'ize')
        elif word.endswith('ation'):
            if self.measure(self.__core(word, 'ation')) > 0:
                word = self.__replace(word, 'ation', 'ate')
        elif word.endswith('ator'):
            if self.measure(self.__core(word, 'ator')) > 0:
                word = self.__replace(word, 'ator', 'ate')
        elif word.endswith('alism'):
            if self.measure(self.__core(word, 'alism')) > 0:
                word = self.__replace(word, 'alism', 'al')
        elif word.endswith('iveness'):
            if self.measure(self.__core(word, 'iveness')) > 0:
                word = self.__replace(word, 'iveness', 'ive')
        elif word.endswith('fulness'):
            if self.measure(self.__core(word, 'fulness')) > 0:
                word = self.__replace(word, 'fulness', 'ful')
        elif word.endswith('ousness'):
            if self.measure(self.__core(word, 'ousness')) > 0:
                word = self.__replace(word, 'ousness', 'ous')
        elif word.endswith('aliti'):
            if self.measure(self.__core(word, 'aliti')) > 0:
                word = self.__replace(word, 'aliti', 'al')
        elif word.endswith('iviti'):
            if self.measure(self.__core(word, 'iviti')) > 0:
                word = self.__replace(word, 'iviti', 'ive')
        elif word.endswith('biliti'):
            if self.measure(self.__core(word, 'biliti')) > 0:
                word = self.__replace(word, 'biliti', 'ble')

        return word

    def step_3(self, word, m):
        if word.endswith('icate'):
            if self.measure(self.__core(word, 'icate')) > 0:
                word = self.__replace(word, 'icate', 'ic')
        elif word.endswith('ative'):
            if self.measure(self.__core(word, 'ative')) > 0:
                word = self.__replace(word, 'ative', '')
        elif word.endswith('alize'):
            if self.measure(self.__core(word, 'alize')) > 0:
                word = self.__replace(word, 'alize', 'al')
        elif word.endswith('iciti'):
            if self.measure(self.__core(word, 'iciti')) > 0:
                word = self.__replace(word, 'iciti', 'ic')
        elif word.endswith('ical'):
            if self.measure(self.__core(word, 'ical')) > 0:
                word = self.__replace(word, 'ical', 'ic')
        elif word.endswith('ful'):
            if self.measure(self.__core(word, 'ful')) > 0:
                word = self.__replace(word, 'ful', '')
        elif word.endswith('ness'):
            if self.measure(self.__core(word, 'ness')) > 0:
                word = self.__replace(word, 'ness', '')

        return word

    def step_4(self, word, m):
        if word.endswith('al'):
            if self.measure(self.__core(word, 'al')) > 1:
                word = self.__replace(word, 'al', '')
        elif word.endswith('ance'):
            if self.measure(self.__core(word, 'ance')) > 1:
                word = self.__replace(word, 'ance', '')
        elif word.endswith('ence'):
            if self.measure(self.__core(word, 'ence')) > 1:
                word = self.__replace(word, 'ence', '')
        elif word.endswith('er'):
            if self.measure(self.__core(word, 'er')) > 1:
                word = self.__replace(word, 'er', '')
        elif word.endswith('ic'):
            if self.measure(self.__core(word, 'ic')) > 1:
                word = self.__replace(word, 'ic', '')
        elif word.endswith('able'):
            if self.measure(self.__core(word, 'able')) > 1:
                word = self.__replace(word, 'able', '')
        elif word.endswith('ible'):
            if self.measure(self.__core(word, 'ible')) > 1:
                word = self.__replace(word, 'ible', '')
        elif word.endswith('ant'):
            if self.measure(self.__core(word, 'ant')) > 1:
                word = self.__replace(word, 'ant', '')
        elif word.endswith('ement'):
            if self.measure(self.__core(word, 'ement')) > 1:
                word = self.__replace(word, 'ement', '')
        elif word.endswith('ment'):
            if self.measure(self.__core(word, 'ment')) > 1:
                word = self.__replace(word, 'ment', '')
        elif word.endswith('ent'):
            if self.measure(self.__core(word, 'ent')) > 1:
                word = self.__replace(word, 'ent', '')
        elif word.endswith('ion'):
            temp = self.__core(word, 'ion')
            if self.measure(temp) > 1:
                if len(temp) > 0 and temp.endswith('t') or temp.endswith('s'):
                    word = self.__replace(word, 'ion', '')
        elif word.endswith('ou'):
            if self.measure(self.__core(word, 'ou')) > 1:
                word = self.__replace(word, 'ou', '')
        elif word.endswith('ism'):
            if self.measure(self.__core(word, 'ism')) > 1:
                word = self.__replace(word, 'ism', '')
        elif word.endswith('ate'):
            if self.measure(self.__core(word, 'ate')) > 1:
                word = self.__replace(word, 'ate', '')
        elif word.endswith('iti'):
            if self.measure(self.__core(word, 'iti')) > 1:
                word = self.__replace(word, 'iti', '')
        elif word.endswith('ous'):
            if self.measure(self.__core(word, 'ous')) > 1:
                word = self.__replace(word, 'ous', '')
        elif word.endswith('ive'):
            if self.measure(self.__core(word, 'ive')) > 1:
                word = self.__replace(word, 'ive', '')
        elif word.endswith('ize'):
            if self.measure(self.__core(word, 'ize')) > 1:
                word = self.__replace(word, 'ize', '')

        return word

    def step_5a(self, word, m):
        if word.endswith('e'):
            if self.measure(self.__core(word, 'e')) > 1:
                word = self.__replace(word, 'e', '')
        elif word.endswith('e') and m == 1 and not self.__o_star(word, 'e'):
            word = self.__replace(word, 'e', '')

        return word

    def step_5b(self, word, m):
        if m > 1 and self.__d_star(word, '') and word.endswith('l'):
            word = word[ : len(word) - 1]

        return word

    def stem(self, word):
        m = self.measure(word)

        word = self.step_1a(word, m)
        word = self.step_1b(word, m)
        word = self.step_1c(word, m)
        word = self.step_2(word, m)
        word = self.step_3(word, m)
        word = self.step_4(word, m)
        word = self.step_5a(word, m)
        word = self.step_5b(word, m)

        return word

    def stem_text(self, text):
        content = text.split()
        new_content = ""

        for word in content:
            new_content += self.stem(word) + " "

        return new_content.strip()
