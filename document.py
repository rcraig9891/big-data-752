from nltk.tokenize import word_tokenize
token_frequency = []


class Document:
    def __init__(self, doc_id, content):
        self.doc_id = doc_id
        self.content = content
        self.tokens = self.parse_words()
        self.tfidf_list = []

    def parse_words(self):
        tokens = []
        words = word_tokenize(self.content)
        for word in words:
            if word != ',' and word != '.':
                tokens.append(word)
        return tokens

    def calculate_tf(self):
        pass

    def calculate_idf(self):
        pass

    def calculate_tfidf(self):
        pass

