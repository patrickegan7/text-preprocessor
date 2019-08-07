from preprocessor import Preprocessor
import os
import shutil

class Tester:
    def __init__(self):
        self.pre_proc = Preprocessor(corpus="test_corpus")

    def run(self, clean=True):
        if clean:
            self.clean()

        self.pre_proc.process_corpus()

    def clean(self):
        path = "processed"

        if os.path.isdir(path):
            shutil.rmtree(path)


tester = Tester()
tester.run(clean=False)
