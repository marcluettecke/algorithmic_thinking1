import matplotlib.pyplot as plt
from application1_loaddata import load_graph, CITATION_URL
from project1 import in_degree_distribution
from matplotlib.ticker import ScalarFormatter


# load the data
def load_data(url=CITATION_URL):
    """

    Args:
        url:

    Returns:

    """
    citation_graph = load_graph(url)
    return in_degree_distribution(citation_graph)


def normalize_data(id_distribution):
    """

    Args:
        id_distribution:

    Returns:

    """
    return {int(k): round(v / float(sum(id_distribution.values())), 4) for k,
                                                                           v in id_distribution.items()}


def visualize_distribution(distribution_dictionary,
                           title="In-degree distribution of the citation graph on a \n log-log scale (base 10)"):
    """

    Args:
        distribution_dictionary:

    Returns:

    """
    fig, ax = plt.subplots()
    # plt.figure()
    ax.loglog(list(distribution_dictionary.keys()),
              list(distribution_dictionary.values()), "o")
    ax.set(xlabel="(Logarithmic) in-degree", ylabel="(Logarithmic) fraction of nodes",
           title=title)
    ax.xaxis.set_major_formatter(ScalarFormatter())
    ax.yaxis.set_major_formatter(ScalarFormatter())

    ax.grid()
    plt.tight_layout()
    plt.show()
    return ax, plt.gcf()


if __name__ == '__main__':
    axes, figure = visualize_distribution(normalize_data(load_data()))
    figure.savefig(fname="./graphs/figure_citation_data.png")
