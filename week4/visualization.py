import matplotlib.pyplot as plt


def visualize_resilience(list_of_resiliences, type_of_attack="random order attack"):
    """

    Args:
        list_of_resiliences:

    Returns:

    """
    plt.figure()
    ax = plt.axes()
    x_range = range(len(list_of_resiliences[0]))

    plt.plot(x_range, list_of_resiliences[0], label="Computer graph")
    plt.plot(x_range, list_of_resiliences[1], label="Randomly generated graph, p = 0.004")
    plt.plot(x_range, list_of_resiliences[2], label="UPA graph, m = 2")

    ax.set(xlabel="Number of servers attacked", ylabel="Remaining resilience, \n i.e. size of largest connected "
                                                       "component",
           title="Behavior of resilience for computer network graph, \n randomly generated graph and UPA graph for "
                 "%s".format(type_of_attack))

    ax.grid()
    plt.tight_layout()
    plt.legend()
    plt.savefig(fname="./graphs/figure_resilience_comparison.png")
    # plt.savefig(fname="./graphs/figure_resilience_comparison_targeted.png")
    plt.show()

    return ax, plt.gcf()


def visualize_run_times(list_of_runtimes):
    """

    Args:
        list_of_runtimes:

    Returns:

    """
    plt.figure()
    ax = plt.axes()
    x_range = range(10, 1000, 10)

    plt.plot(x_range, list_of_runtimes[0], label="Run times for 'targeted_order'")
    plt.plot(x_range, list_of_runtimes[1], label="Run times for 'Fast_targeted_order'")

    ax.set(xlabel="Number of nodes in graph", ylabel="Run time in seconds",
           title="Runtime (measured by the timeit Python package) comparison \n for the targeted_order and "
                 "fast_targeted_order algorithm \n of increasingly complex DPA graphs")

    ax.grid()
    plt.tight_layout()
    plt.legend()
    plt.savefig(fname="./graphs/figure_runtime_comparison.png")
    plt.show()

    return ax, plt.gcf()


if __name__ == '__main__':
    # axes, figure = visualize_resilience([[1, 2, 3, 4], [100, 6, 7, 8]])
    # figure.savefig(fname="./graphs/figure_citation_data.png")
    pass
