import numpy as np
import matrix_version as mv
import queries as qu
from graph_db import driver, close_driver

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
    print(url_list)
    establish_links()
    close_driver()


def fetch_nodes():
    with driver.session() as session:
        nodes = session.execute_read(qu.get_nodes)
        return nodes


def establish_links():
    with driver.session() as session:
        map_input = session.execute_read(qu.get_linked_nodes, 'youtube.com')
        print(map_input)


if __name__ == "__main__":
    main()

