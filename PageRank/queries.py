def get_nodes(tx):
    result = tx.run("MATCH (n:URL) RETURN n.name AS name")
    return [record["name"] for record in result]

