# big-data-752
Extracircular challenges for COMPSCI 752. These are personal projects using the knowledge learnt from COMPSCI 752 (big data management).

# Challenge One: Near Duplicate Detection (Package: TFIDF)
10 Chat GPT bots were provided the exact same prompt by the user ("give me a short paragraph on the corona virus").Each response by the chat bots are treated as there own individual document. Responses provided in gpt.response.py file for testing purposes. You could call the OpenAi API, however to my knowledge this is not a free service.

The challenge is how can we measure the similarity between these documents in an efficent manner. MapReduce provides a framework for processing large datasets in parrallel using distirbuted computing. From a practicl perspective this informantion can be used to assit in plagerism detection.

# Step One: Calculate TFIDF results for each document
TF-IDF, stands for Term Frequency-Inverse Document Frequency. It is statistical measure used in text mining and information retrieval to evaluate the importance of a word in a document relative to a collection of documents. It combines two metrics: term frequency (TF) and inverse document frequency (IDF).

Only relevant terms are required for this process, stop words and abraviations are removed using the NLTK package.

TF is calculated using the frequency of a word divided the total words in the document. IDF is calculated as the logarithm of the total number of documents divided by the number of documents containing the term. IDF works on the theory that terms that occur less frequently accoss documents tend to be more important.

# Step Two: Compute Similarity between documents
The dot product (sum of multiplication of matching key values) of the TFIDF for each document is used to determine how similar each pair of documents are.
Example of dot product is term1 in doc 1 x term1 in doc2 + term2 in doc1 x term2 in doc2 and so on.

# Challenge Two: PageRank Algorithms (Package: PageRank)




