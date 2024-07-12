import numpy as np
import page_rank as pr
import queries as qu
from neo4j import GraphDatabase

tr_matrix = np.array([
    [0,     0,  0, (1/3),  1],    # A
    [1,     0,  1,     0,  0],    # B
    [0, (1/2),  0, (1/3),  0],    # C
    [0, (1/2),  0,     0,  0],    # D
    [0,     0,  0, (1/3),  0]     # E
])
u_size = tr_matrix.shape[0]
damp_factor = 0
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))


def main():
    # Matrix Version
    ranks = pr.page_rank(tr_matrix, u_size, damp_factor)
    pages = ['A', 'B', 'C', 'D', 'E']
    for (page, value) in zip(pages, ranks):
        print(f'Page {page}: {value}')
    # Map_Reduce Version
    url_list = fetch_nodes()
    map_input = establish_links(url_list)
    driver.close()
    pr.map_reduce(map_input)


def fetch_nodes():
    with driver.session() as session:
        nodes = session.execute_read(qu.get_nodes)
        return nodes


def establish_links(urls):
    map_hyperlinks = {}
    with driver.session() as session:
        for url in urls:
            hyper_links = session.execute_read(qu.get_linked_nodes, url)
            map_hyperlinks[url, 1/len(urls)] = hyper_links
    print(map_hyperlinks)
    return map_hyperlinks


if __name__ == "__main__":
    main()

