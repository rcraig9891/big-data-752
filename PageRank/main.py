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
    establish_links(url_list)
    close_driver()


def fetch_nodes():
    with driver.session() as session:
        nodes = session.execute_read(qu.get_nodes)
        return nodes


def establish_links(urls):
    map_hyperlinks = {}
    with driver.session() as session:
        for url in urls:
            hyper_links = session.execute_read(qu.get_linked_nodes, url)
            map_hyperlinks[url] = hyper_links
    return map_hyperlinks


if __name__ == "__main__":
    main()

