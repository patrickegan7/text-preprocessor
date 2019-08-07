class StopWordRemover:
    def __init__(self):
        self.stop_words = self.__create_stop_words()

    def is_stop_word(self, word):
        return word in self.stop_words

    def push_stop_word(self, word):
        if isinstance(word, str):
            self.stop_words.add(word)
        elif isinstance(word, set):
            self.stop_words = self.stop_words.union(word)
        elif isinstance(word, list) or isinstance(word, tuple):
            self.stop_words = self.stop_words.union(set(word))

    def pop_stop_word(self, word):
        if isinstance(word, str):
            self.stop_words.discard(word)

    def remove_stop_words(self, text):
        content = text.split()
        new_content = ""
        for word in content:
            if not self.is_stop_word(word):
                new_content += word + " "

        return new_content.strip()


    # Created to have list at the end of the file
    def __create_stop_words(self):
        # Taken from NLTK's list of English stop words
        return {"i",
        "me",
        "my",
        "myself",
        "we",
        "our",
        "ours", "ourselves",
        "you",
        "your",
        "yours",
        "yourself",
        "yourselves",
        "he",
        "him",
        "his",
        "himself",
        "she",
        "her",
        "hers",
        "herself",
        "it",
        "its",
        "itself",
        "they",
        "them",
        "their",
        "theirs",
        "themselves",
        "what",
        "which",
        "who",
        "whom",
        "this",
        "that",
        "these",
        "those",
        "am",
        "is",
        "are",
        "was",
        "were",
        "be",
        "been",
        "being",
        "have",
        "has",
        "had",
        "having",
        "do",
        "does",
        "did",
        "doing",
        "a",
        "an",
        "the",
        "and",
        "but",
        "if",
        "or",
        "because",
        "as",
        "until",
        "while",
        "of",
        "at",
        "by",
        "for",
        "with",
        "about",
        "against",
        "between",
        "into",
        "through",
        "during",
        "before",
        "after",
        "above",
        "below",
        "to",
        "from",
        "up",
        "down",
        "in",
        "out",
        "on",
        "off",
        "over",
        "under",
        "again",
        "further",
        "then",
        "once",
        "here",
        "there",
        "when",
        "where",
        "why",
        "how",
        "all",
        "any",
        "both",
        "each",
        "few",
        "more",
        "most",
        "other",
        "some",
        "such",
        "no",
        "nor",
        "not",
        "only",
        "own",
        "same",
        "so",
        "than",
        "too",
        "very",
        "s",
        "t",
        "can",
        "will",
        "just",
        "don",
        "should",
        "now"}
