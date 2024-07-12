import numpy as np
import matrix_version as mv
from graph_db import driver, close_driver
import queries

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
    url_list = fetch_nodes()
    close_driver()


def fetch_nodes():
    with driver.session() as session:
        nodes = session.read_transaction(queries.get_nodes)
        return nodes


if __name__ == "__main__":
    main()

