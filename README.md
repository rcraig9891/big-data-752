# big-data-752
Extracircular challenges for COMPSCI 752. These are personal projects using the knowledge learnt from COMPSCI 752 (big data management).

# Challenge One: MapReduce Near Duplicate Detection
10 Chat GPT bots were provided the exact same prompt by the user ("give me a short paragraph on the corona virus").Each response by the chat bots are treated as there own individual document. Responses provided in gpt.response.py file for testing purposes.

The challenge is how can we measure the similarity between these documents in an efficent manner. MapReduce provides a framework for processing large datasets in parrallel using distirbuted computing. From a practicl perspective this informantion can be used to assit in plagerism detection.

# Step One: Calculate TFIDF (tfidf.py)
TF-IDF, stands for Term Frequency-Inverse Document Frequency. It is statistical measure used in text mining and information retrieval to evaluate the importance of a word in a document relative to a collection of documents. It combines two metrics: term frequency (TF) and inverse document frequency (IDF).

TF is calculated using the frequency of a word divided the total words in the document. IDF is calculated as the logarithm of the total number of documents divided by the number of documents containing the term. IDF works on the theory that terms that occur less frequently accoss documents tend to be more important.




