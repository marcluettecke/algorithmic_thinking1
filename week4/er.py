from computer_data import load_graph, NETWORK_URL
import random


def make_random_undirected_graph(num_nodes, probability):
    """
    Function to generate a dictionary of a fully connected (undirected) graph with a specific number of nodes.
    Args:
        probability:
        num_nodes: int value of nodes

    Returns:
        Dictionary of fully connected, directed graph with num_nodes nodes.
    """
    assert num_nodes >= 0
    graph_dictionary = {}
    # establish dictionary
    for i in range(num_nodes):
        graph_dictionary[i] = set()

    for node in range(num_nodes):
        sub_connections = range(num_nodes)
        sub_connections.remove(node)
        for j in sub_connections:
            threshold = random.uniform(0, 1)
            # have to halve the probability, because we are going through all nodes and are therefore double-counting
            if threshold < probability/2:
                graph_dictionary[node].add(j)
                graph_dictionary[j].add(node)
    return graph_dictionary


if __name__ == '__main__':
    print make_random_undirected_graph(10, probability=0.5)
