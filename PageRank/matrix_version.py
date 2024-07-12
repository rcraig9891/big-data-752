import numpy as np


def page_rank(matrix, start_factor, d_factor, convergence=1e-6):
    iteration = 1
    pr_vector = np.ones(start_factor) / start_factor
    print(f'Vector 0= {pr_vector}')

    while True:
        old_vector = pr_vector.copy()
        matrix_calc = (1-d_factor)/start_factor + d_factor * matrix
        pr_vector = np.dot(matrix_calc, pr_vector)

        if np.sum(abs(pr_vector - old_vector)) < convergence:
            break

    return pr_vector
