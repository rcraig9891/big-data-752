def map_function(graph):
    map_output = []
    print(graph)
    for key in graph:
        map_output.append((key[0], graph[key]))
        link_list = graph[key]
        for link in link_list:
            pass


def reduce_function(map_output):
    pass

