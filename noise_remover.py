from string import punctuation

class NoiseRemover:
    def __init__(self, document):
        self.doc = document
        self.exceptions = {"ph.d.", "u.s.a.", "u.k."} # TODO: need to fill this out
        self.noise = set(punctuation)

    def remove_noise(self):
        contents = self.doc.split()

        for word in contents:
            if not word in self.exceptions:
                for char in word:
                    if char in self.noise:
                        word.replace(char, "")

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
