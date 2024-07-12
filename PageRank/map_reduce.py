def map_function(graph):
    node_links = []
    node_scores = {}
    for key in graph:
        node_links.append((key[0], graph[key]))
        node_scores[key[0]] = key[1]
    print(node_links)


def reduce_function(map_output):
    pass

