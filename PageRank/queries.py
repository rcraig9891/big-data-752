def get_nodes(tx):
    result = tx.run("MATCH (n:URL) RETURN n.name AS name")
    return [record["name"] for record in result]


def get_linked_nodes(tx, node):
    result = tx.run("MATCH (a)-[:LINK]->(b) WHERE a.name = $nodeName RETURN b.name AS linkedNode", nodeName=node)
    return [record["linkedNode"] for record in result]