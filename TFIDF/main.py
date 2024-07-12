import gpt_response as gpt
import document as doc
import math
similar_documents = []
idf_scores = {}


def main():
    doc1 = doc.Document(1, gpt.d1)
    doc2 = doc.Document(2, gpt.d2)
    doc3 = doc.Document(3, gpt.d3)
    doc4 = doc.Document(4, gpt.d4)
    doc5 = doc.Document(5, gpt.d5)
    doc6 = doc.Document(6, gpt.d6)
    doc7 = doc.Document(7, gpt.d7)
    doc8 = doc.Document(8, gpt.d8)
    doc9 = doc.Document(9, gpt.d9)
    doc10 = doc.Document(10, gpt.d10)
    documents = [doc1, doc2, doc3, doc4, doc5, doc6, doc7, doc8, doc9, doc10]
    calculate_idf(documents)
    for document in documents:
        term_frequency = document.term_frequency()
        document.calculate_tf(term_frequency)
        document.calculate_tfidf(idf_scores)


def calculate_idf(doc_list):
    for document in doc_list:
        token_set = set(document.tokens)
        for token in token_set:
            if token in idf_scores:
                idf_scores[token] += 1
            else:
                idf_scores[token] = 1
    for term in idf_scores:
        idf_scores[term] = round(math.log2(len(doc_list)/idf_scores[term]), 2)


if __name__ == "__main__":
    main()

