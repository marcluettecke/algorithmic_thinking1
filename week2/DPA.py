from week2.DPA_helper import DPATrial
from week2.project1 import make_complete_graph, in_degree_distribution
from week2.visualize_edges import normalize_data, visualize_distribution


def make_weighted_graph(num_nodes_full_connected, num_nodes_total):
    """

    Args:
        num_nodes_full_connected:
        num_nodes_total:

    Returns:

    """
    # generate complete graph with n nodes
    complete_graph = make_complete_graph(num_nodes=num_nodes_full_connected)
    dpa_instance = DPATrial(num_nodes_full_connected)
    for i in range(num_nodes_full_connected, num_nodes_total):
        complete_graph[i] = dpa_instance.run_trial(num_nodes=num_nodes_total)
    return complete_graph


if __name__ == '__main__':
    graph_dictionary = make_weighted_graph(num_nodes_full_connected=50, num_nodes_total=10000)
    normalized_distribution = normalize_data(in_degree_distribution(graph_dictionary))
    axes, figure = visualize_distribution(normalized_distribution, title="In-degree distribution of the constructed "
                                                                         "DPA graph on a \n log-log scale (base 10)")
    figure.savefig(fname="../graphs/figure_dpa_data.png")
