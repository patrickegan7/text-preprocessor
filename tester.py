from preprocessor import Preprocessor

class Tester:
    def __init__(self):
        self.pre_proc = Preprocessor(corpus="test_corpus")

    def run(self):
        self.pre_proc.process_corpus()

tester = Tester()
tester.run()
