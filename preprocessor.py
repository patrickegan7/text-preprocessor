from contraction_expander import ContractionExpander
from stop_word_remover import StopWordRemover
from noise_remover import NoiseRemover
from stemmer import Stemmer
from pathlib import Path
import shutil

class Preprocessor:
    def __init__(self, corpus=None):
        if corpus != None:
            self.corpus_path = Path(str(corpus))
        else:
            self.corpus_path = None

        self.contraction_expansion_flag = False
        self.stop_word_flag = False
        self.noise_removal_flag = False
        self.stemmer_flag = False

        # default, use all preprocessing techniques
        if len(sys.argv) == 0:
            self.contraction_expansion_flag = True
            self.contraction_expander = ContractionExpander()

            self.stop_word_flag = True
            self.stop_word_remover = StopWordRemover()

            self.noise_removal_flag = True
            self.noise_remover = NoiseRemover()

            self.stemmer_flag = True
            self.stemmer = Stemmer()

        else:
            for arg in sys.argv:
                if arg == "-cxp":
                    self.contraction_expansion_flag = True
                    self.contraction_expander = ContractionExpander()

                elif arg == "-swr":
                    self.stop_word_flag = True
                    self.stop_word_remover = StopWordRemover()

                elif arg = "-nr":
                    self.noise_removal_flag = True
                    self.noise_remover = NoiseRemover()

                elif arg = "-stem":
                    self.stemmer_flag = True
                    self.stemmer = Stemmer()

    # uses
    def process_corpus(self):
        if self.corpus_path == None:
            raise Exception('Please set the path to the corpus first')

        processed_path = self.corpus_path / "processed"
        processed_path.mkdir()

        # assumes that everything in corpus_path is not a file, not a directory
        for file in self.corpus_path.iterdir():
            with open(file, 'r') as f:
                content = f.read()

                if self.noise_removal_flag:
                    content = self.noise_remover.remove_noise(content)

                if self.contraction_expansion_flag:
                    content = self.contraction_expander.expand_text(content)

                new_content = ''

                if self.stop_word_flag and self.stemmer_flag:
                    for word in content:
                        if not self.stop_word_remover.is_stop_word(word):
                            new_content += self.stemmer.stem(word)
                    content = new_content

                elif self.stop_word_flag:
                    for word in content:
                        if not self.stop_word_remover.is_stop_word(word):
                            new_content += word
                    content = new_content

                elif self.stemmer_flag:
                    for word in content:
                        new_content += self.stemmer.stem(word)
                    content = new_content

                new_file = open(str(file) + "_processed", -w)
                new_file.write(content)

                shutil.move(str(new_file), str(processed_path) + "/" + str(new_file))


    # takes in the folder for corpus
    def set_path(self, corpus):
        if corpus == None:
            raise Exception('Corpus was None, please give a directory for the corpus')

        if isinstance(corpus, str):
            self.corpus_path = Path(corpus)
        elif isinstance(corpus, Path):
            self.corpus_path = corpus
        else:
            raise Exception('Invalid type for corpus, please give a Path or a string')
