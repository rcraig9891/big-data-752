import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

token_frequency = []


class Document:
    def __init__(self, doc_id, content):
        self.doc_id = doc_id
        self.content = content
        self.tokens = self.parse_words()
        self.tfidf_list = []

    def parse_words(self):
        processed_words = []
        words = word_tokenize(self.content)
        stop_words = set(stopwords.words('english'))
        tokens = [word for word in words if word.lower() not in stop_words]
        for token in tokens:
            if token != ',' and token != '.':
                processed_words.append(token)
        return processed_words

    def term_frequency(self):
        dictionary = {}
        for token in self.tokens:
            if token in dictionary:
                dictionary[token] += 1
            else:
                dictionary[token] = 1
        return dictionary

    def calculate_tf(self, term_dict):
        length = len(self.tokens)
        for key in term_dict:
            term_dict[key] = round(term_dict[key]/length, 2)
        return term_dict

    def calculate_tfidf(self):
        pass

