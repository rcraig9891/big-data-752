import numpy as np

d_factor = 1
convergence = 1e-6


def page_rank(matrix, start_factor):
    pr_vector = np.ones(start_factor) / start_factor
    while True:
        old_vector = pr_vector.copy()
        matrix_calc = (1-d_factor)/start_factor + d_factor * matrix
        pr_vector = np.dot(matrix_calc, pr_vector)
        if np.sum(abs(pr_vector - old_vector)) < convergence:
            break
    return pr_vector


def map_reduce(graph_result):
    node_links = {}
    node_scores = {}
    previous_pr = np.ones(len(graph_result))/len(graph_result)
    # Process multiple times to reach convergence
    for key, value in graph_result.items():
        webpage = key[0]
        pr_score = key[1]
        node_links[webpage] = graph_result[key]
        for link in value:
            if link in node_scores:
                node_scores[link] += round((d_factor * pr_score + 1 - d_factor)/len(value), 1)
            else:
                node_scores[link] = pr_score/len(value)




