from stemmer import Stemmer
class StemTester:
    def __init__(self):
        self.s = Stemmer()

    def test_step1a(self,word):
        m = s.measure(word)
        ret = [self.s.step_1a(word, m), m]
        return ret

    def test_step1b(self, word):
        temp = self.test_step1a(word)
        ret = [self.s.step_1b(temp[0], temp[1]), temp[1]]
        return ret

    def test_step1c(self, word):
        temp = self.test_step1b(word)
        ret = [self.s.step_1c(temp[0], temp[1]), temp[1]]
        return ret

    def test_step2(self, word):
        temp = self.test_step1c(self, word)
        ret = [self.s.step_2(temp[0], temp[1]), temp[1]]
        return ret

    def test_step3(self, word):
        temp = self.test_step2(self, word)
        ret = [self.s.step_3(temp[0], temp[1]), temp[1]]
        return ret

    def test_step4(self, word):
        temp = self.test_step3(self, word)
        ret = [self.s.step_4(temp[0], temp[1]), temp[1]]
        return ret

    def test_step5a(self, word):
        temp = self.test_step4(self, word)
        ret = [self.s.step_5a(temp[0], temp[1]), temp[1]]
        return ret

    def test_step5b(self, word):
        temp = self.test_step5a(self, word)
        ret = [self.s.step_5b(temp[0], temp[1]), temp[1]]
        return ret
