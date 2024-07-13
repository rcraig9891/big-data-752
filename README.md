# big-data-752
These are personal projects using the knowledge learnt from COMPSCI 752 (big data management).

# Challenge One: Near Duplicate Detection (Package: TFIDF)
10 Chat GPT bots were provided the exact same prompt by the user ("give me a short paragraph on the corona virus").Each response by the chat bots are treated as there own individual document. Responses provided in gpt.response.py file for testing purposes. You could call the OpenAi API, however to my knowledge this is not a free service.

The challenge is how can we measure the similarity between these documents in an efficent manner. MapReduce provides a framework for processing large datasets in parrallel using distirbuted computing. From a practicl perspective this informantion can be used to assit in plagerism detection.

# Step One: Calculate TFIDF results for each document
TF-IDF, stands for Term Frequency-Inverse Document Frequency. It is statistical measure used in text mining and information retrieval to evaluate the importance of a word in a document relative to a collection of documents. It combines two metrics: term frequency (TF) and inverse document frequency (IDF).

Only relevant terms are required for this process, stop words and abraviations are removed using the NLTK package.

TF is calculated using the frequency of a word divided the total words in the document. IDF is calculated as the logarithm of the total number of documents divided by the number of documents containing the term. IDF works on the theory that terms that occur less frequently accoss documents tend to be more important.

# Step Two: Compute Similarity between documents
The dot product (sum of multiplication of matching key values) of the TFIDF for each document is used to determine how similar each pair of documents are.
Example of dot product is term1 in doc 1 x term1 in doc2 + term2 in doc1 x term2 in doc2 and so on. Now we have a formal statistical measurment of the similarity of the document pairs, which could easily be converted to JSON.

# Challenge Two: PageRank Algorithms (Package: PageRank)
PageRank forms the basis of Google's original search algorithm, influencing the ranking of search results based on the importance of pages. PageRank assigns a numerical weight or importance to each page on the web based on the number and quality of links pointing to it. PageRank assigns each page a score, which represents the probability that a user randomly clicking links will arrive at that page. The score is calculated iteratively and converges to a stable value over time. 

# Step One: Matrix Version
Calculate the page ranks of a matrix representation using numPy library. Columns represent a starting point for the surfer while rows represent the probability of an end point relative to the column.

# Step Two: Graph Version
This time we will implement the pageRank algorithm on an actual graph database. The graph is displayed in the image neo4j_db.png file. We will apply Cypher queries to retireve the information needed then apply a sudo map_reduce function to determine the page ranks for the nodes in the graph.

# Challenge Three: Implement the Bloom Filter
A Bloom filter is a probabilistic data structure designed to efficiently test whether an element is a member of a set. It can quickly determine membership with a possibility of false positives but guarantees no false negatives. Uses a bit array (efficent storage) and multiple hash functions to store information about the presence of elements. Query and insertion operations are in constant time making them an efficent filter.

Hash functions use the input value and return an integer. That integer is used as the index in the bloom filter where that index is set to 1. This is done accross multiple hash functions. For an input to return a positive (might exist in set) all hash functions must return integers where the index in the bloom filter are set to 1. Multiple hash functions can reduce the probability of collisions (false positives).

Avoid unnecessary disk lookup in databases. Bloom Filter is used to filter lookups that do not exist in the dataset. Bloom Filter can check if email exists in dataset to filter out malicious emails. 

# Step One: Create the Bloom Filter
Implement a spam filter for emails (valid emails are stored in a list). These emails will be processed through the hash functions which will update the indexes in the bloom filter. mmh3 is a Python library that implements the MurmurHash3 algorithm and can be used to produce a hash value that can set the index. Using seed as an additional input will alter the hash output. 

# Step Two: Create a GUI to test the Bloom Filter
Implement a GUI where the user can input an email address to check if it might be in the list. The GUI will return True if it might exist or False if it definitly does not (Bloom Filter never has false negatives).






