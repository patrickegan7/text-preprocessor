from contraction_expander import ContractionExpander
from stop_word_remover import StopWordRemover
from noise_remover import NoiseRemover
from pathlib import Path

class Preprocessor:
    def __init__(self, folder):
        self.corpus_path = Path(str(folder))

        contraction_expansion_flag = False
        stop_word_flag = False
        noise_removal_flag = False

        for arg in sys.argv:
            if arg == "-cxp":
                contraction_expansion_flag = True
                self.contraction_expander = ContractionExpander()

            elif arg == "-swr":
                stop_word_flag = True
                self.stop_word_remover = StopWordRemover()

            elif arg = "-nr":
                noise_removal_flag = True
                self.noise_remover = NoiseRemover()
