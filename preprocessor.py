from contraction_expander import ContractionExpander
from stop_word_remover import StopWordRemover
from noise_remover import NoiseRemover
from stemmer import Stemmer
from pathlib import Path
import shutil
import sys
from os import path

class Preprocessor:
    def __init__(self, corpus=None, cxp=True, swr=True, nr=True, stem=True):
        if corpus != None:
            self.corpus_path = Path(str(corpus))
        else:
            self.corpus_path = None

        self.contraction_expansion_flag = False
        self.stop_word_flag = False
        self.noise_removal_flag = False
        self.stemmer_flag = False

        if cxp:
            self.contraction_expansion_flag = True
            self.contraction_expander = ContractionExpander()
        if swr:
            self.stop_word_flag = True
            self.stop_word_remover = StopWordRemover()
        if nr:
            self.noise_removal_flag = True
            self.noise_remover = NoiseRemover()
        if stem:
            self.stemmer_flag = True
            self.stemmer = Stemmer()

    def process_corpus(self):
        if self.corpus_path == None:
            raise Exception('Please set the path to the corpus first')

        processed_path = Path("processed")
        if(not Path(str(processed_path)).exists()):
            processed_path.mkdir()

        # assumes that everything in corpus_path is not a file, not a directory
        for file in self.corpus_path.iterdir():
            with open(file, 'r') as f:
                content = f.read().lower()

                if self.noise_removal_flag:
                    content = self.noise_remover.remove_noise(content)

                if self.contraction_expansion_flag:
                    content = self.contraction_expander.expand_text(content)
                new_content = ''

                if self.stop_word_flag:
                    content = self.stop_word_remover.remove_stop_words(content)

                if self.stemmer_flag:
                    content = self.stemmer.stem_text(content)

                new_file = open("processed\\" + path.basename(f.name), 'w')
                new_file.write(content)
                new_file.close()

                #shutil.move(str(new_file), str(processed_path) + str(new_file))


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
