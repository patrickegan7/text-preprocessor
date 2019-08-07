from string import punctuation


class NoiseRemover:
    def __init__(self):
        self.exceptions = {"ph.d.", "u.s.a.", "u.k."} # TODO: need to fill this out
        self.exceptions = self.__add_contractions_to_exceptions()
        self.noise = set(punctuation)

    def remove_noise(self, document):
        contents = document.split()

        for idx, word in enumerate(contents):
            if not word in self.exceptions:
                for char in word:
                    if char in self.noise:
                        contents[idx] = word.replace(char, "")

        # reassemble string array into one string
        new_contents = ""
        for word in contents:
            new_contents += word + " "

        return new_contents.strip()

    def push_noise(self, noise):
        if isinstance(noise, str):
            self.noise.add(noise)
        elif isinstance(noise, set):
            self.noise = self.noise.union(noise)
        elif isinstance(noise, list) or isinstance(noise, tuple):
            self.noise = self.noise.union(set(list))

    def pop_noise(self, noise):
        if isinstance(noise, str):
            self.noise.discard(noise)

    # needed so we can perform contraction expansion
    def __add_contractions_to_exceptions(self):
        contractions = {
        "ain't",
        "aren't",
        "can't",
        "can't've",
        "'cause",
        "could've",
        "couldn't",
        "couldn't've",
        "didn't",
        "doesn't",
        "don't",
        "hadn't",
        "hadn't've",
        "hasn't",
        "haven't",
        "he'd",
        "he'd've",
        "he'll",
        "he'll've",
        "he's",
        "how'd",
        "how'd'y",
        "how'll",
        "how's",
        "I'd",
        "I'd've",
        "I'll",
        "I'll've",
        "I'm",
        "I've",
        "isn't",
        "it'd",
        "it'd've",
        "it'll",
        "it'll've",
        "it's",
        "let's",
        "ma'am",
        "mayn't",
        "might've",
        "mightn't",
        "mightn't've",
        "must've",
        "mustn't",
        "mustn't've",
        "needn't",
        "needn't've",
        "o'clock",
        "oughtn't",
        "oughtn't've",
        "shan't",
        "sha'n't",
        "shan't've",
        "she'd",
        "she'd've",
        "she'll",
        "she'll've",
        "she's",
        "should've",
        "shouldn't",
        "shouldn't've",
        "so've",
        "so's",
        "that'd",
        "that'd've",
        "that's",
        "there'd",
        "there'd've",
        "there's",
        "they'd",
        "they'd've",
        "they'll",
        "they'll've",
        "they're",
        "they've",
        "to've",
        "wasn't",
        "we'd",
        "we'd've",
        "we'll",
        "we'll've",
        "we're",
        "we've",
        "weren't",
        "what'll",
        "what'll've",
        "what're",
        "what's",
        "what've",
        "when's",
        "when've",
        "where'd",
        "where's",
        "where've",
        "who'll",
        "who'll've",
        "who's",
        "who've",
        "why's",
        "why've",
        "will've",
        "won't",
        "won't've",
        "would've",
        "wouldn't",
        "wouldn't've",
        "y'all",
        "y'alls",
        "y'all'd",
        "y'all'd've",
        "y'all're",
        "y'all've",
        "you'd",
        "you'd've",
        "you'll",
        "you'll've",
        "you're",
        "you've"
        }

        return self.exceptions.union(contractions)
