"""
Project file for the practice of directed graph and their respective edge distribution.
"""
EX_GRAPH0 = {0: {1, 2},
             1: set(),
             2: set()}
EX_GRAPH1 = {0: {1, 4, 5},
             1: {2, 6},
             2: {3},
             3: {0},
             4: {1},
             5: {2},
             6: set()}
EX_GRAPH2 = {0: {1, 4, 5},
             1: {2, 6},
             2: {3, 7},
             3: {7},
             4: {1},
             5: {2},
             6: set(),
             7: {3},
             8: {1, 2},
             9: {0, 3, 4, 5, 6, 7}}


def make_complete_graph(num_nodes):
    """
    Function to generate a dictionary of a fully connected (directed) graph with a specific number of nodes.
    Args:
        num_nodes: int value of nodes

    Returns:
        Dictionary of fully connected, directed graph with num_nodes nodes.
    """
    assert num_nodes >= 0
    return {node: {other_node for other_node in range(num_nodes) if other_node != node} for node in range(num_nodes)}


def compute_in_degrees(digraph):
    """
    Function to compute the number of in_degrees of a directed graph in dictionary form.
    Args:
        digraph: graph as dictionary. keys are nodes, values are out degrees.

    Returns:
        dictionary with same nodes as input graph, but count of in-degrees of given node in entire graph.
    """

    in_degree = {}
    all_vertex = digraph.keys()

    for dummy_vertex in all_vertex:
        in_degree[dummy_vertex] = 0

    for dummy_vertex in all_vertex:
        for dummy_element in digraph[dummy_vertex]:
            in_degree[dummy_element] += 1

    return in_degree


def in_degree_distribution(digraph):
    """
    Function to find the distribution of in-degrees of a given graph.
    Args:
        digraph: graph as dictionary. keys are nodes, values are out degrees.

    Returns:
        dictionary with values of in-degrees occurring as keys and respective counts how many nodes have this
        in-degree as values.
    """
    in_degree = compute_in_degrees(digraph)
    all_vertex = in_degree.keys()
    degree_dist = {}

    for dummy_vertex in all_vertex:
        degree_value = in_degree[dummy_vertex]

        if degree_dist.has_key(degree_value):
            degree_dist[degree_value] += 1
        else:
            degree_dist[degree_value] = 1

    return degree_dist

# if __name__ == '__main__':
#     test = make_complete_graph(4)
#     print compute_in_degrees(EX_GRAPH2)
#     print in_degree_distribution(EX_GRAPH2)
