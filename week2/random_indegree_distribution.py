import random
from visualize_edges import visualize_distribution, normalize_data
from project1 import in_degree_distribution
import matplotlib.pyplot as plt


def make_random_directed_graph(num_nodes, probability):
    """
    Function to generate a dictionary of a fully connected (directed) graph with a specific number of nodes.
    Args:
        probability:
        num_nodes: int value of nodes

    Returns:
        Dictionary of fully connected, directed graph with num_nodes nodes.
    """
    assert num_nodes >= 0
    graph_dictionary = {}
    for i in range(num_nodes):
        graph_dictionary[i] = set()
        sub_connections = range(num_nodes)
        sub_connections.remove(i)
        for j in sub_connections:
            threshold = random.uniform(0, 1)
            if threshold < probability:
                graph_dictionary[i].add(j)
    return graph_dictionary


def compare_distributions(num_nodes, list_of_probs):
    """

    Args:
        num_nodes:
        list_of_probs:

    Returns:

    """
    for prob in list_of_probs:
        temp_distribution = in_degree_distribution(make_random_directed_graph(num_nodes=num_nodes, probability=prob))
        normalized_temp_distribution = normalize_data(temp_distribution)
        ax, current_fig = visualize_distribution(normalized_temp_distribution)

        ax.set(title="Random graph distribution on log scale (base 10) \n For {} nodes with {} probability of "
                     "connection".format(num_nodes, prob))
        plt.xticks(visible=True)
        current_fig.savefig(fname="./graphs/figure_nodes{}_prob{}.png".format(num_nodes, prob))


if __name__ == '__main__':
    # make_random_directed_graph(num_nodes=5000, probability=0.1)
    compare_distributions(num_nodes=10000, list_of_probs=[0.1, 0.25, 0.5, 0.75, 0.9])
