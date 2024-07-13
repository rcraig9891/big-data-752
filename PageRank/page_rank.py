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


def map_reduce(hyper_links):
    page_ranks = np.ones(len(hyper_links))/len(hyper_links)
    node_scores = {key: rank for key, rank in zip(hyper_links, page_ranks)}
    # Map Portion
    new_scores = {}
    for key, value in hyper_links.items():
        for link in value:
            if link in new_scores:
                new_scores[link] += (d_factor * node_scores[key] + 1 - d_factor) / len(value)
            else:
                new_scores[link] = node_scores[key] / len(value)

