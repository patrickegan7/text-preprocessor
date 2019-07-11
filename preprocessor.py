from contraction_expander import ContractionExpander

class Preprocessor:
    def __init__(self):
        contraction_expansion_flag = False

        for arg in sys.argv:
            if arg == "-cxp":
                contraction_expansion_flag = True
                self.contraction_expander = ContractionExpander()
