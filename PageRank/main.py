import numpy as np
import matrix_version as mv
tr_matrix = np.array([
    [0,     0,  0, (1/3),  1],    # A
    [1,     0,  1,     0,  0],    # B
    [0, (1/2),  0, (1/3),  0],    # C
    [0, (1/2),  0,     0,  0],    # D
    [0,     0,  0, (1/3),  0]     # E
])
u_size = tr_matrix.shape[0]
damp_factor = 0


def main():
    pr = mv.page_rank(tr_matrix, u_size, damp_factor)
    pages = ['A', 'B', 'C', 'D', 'E']

    for (page, value) in zip(pages, pr):
        print(f'Page {page}: {value}')


if __name__ == "__main__":
    main()