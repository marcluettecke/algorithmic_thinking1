from __future__ import division
from project2 import compute_resilience
from computer_data import load_graph, NETWORK_URL, delete_node, copy_graph, targeted_order, fast_targeted_order
from er import make_random_undirected_graph
from visualization import visualize_resilience, visualize_run_times
from upa import ugraph_UPA
import random
import timeit


def random_order(ugraph):
    """

    Args:
        ugraph:

    Returns:

    """
    list_nodes = ugraph.keys()
    random.shuffle(list_nodes)
    return list_nodes


def targeted_order(ugraph):
    '''
    Compute a targeted attack order consisting of
    nodes of maximal degree
    return a list nodes
    '''
    new_graph = copy_graph(ugraph)

    order = []
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node

        delete_node(new_graph, max_degree_node)
        order.append(max_degree_node)
    return order


def degrees_ugraph(ugraph):
    '''
    Take a ugraph
    return {node : degree}
    '''
    degrees = {}
    for node in ugraph:
        degrees[node] = len(ugraph[node])
    return degrees


def fast_targeted_order(ugraph):
    '''
    a fast way to return a list of the nodes
    with descending order
    '''
    degrees = degrees_ugraph(ugraph)
    degree_sets = {}
    degree_max = max(degrees.values())
    for item in range(degree_max + 1):
        degree_sets[item] = set([k for k, v in degrees.items() if v == item])

    L = []
    i = 0
    for k in range(degree_max, -1, -1):
        while degree_sets[k]:
            u = degree_sets[k].pop()
            for v in ugraph[u]:
                d = [key for key, value in degree_sets.items() if v in value][0]
                degree_sets[d].remove(v)
                degree_sets[d - 1].add(v)

            L.append(u)
            i += 1
            delete_node(ugraph, u)

    return L


if __name__ == '__main__':
    # Problem 1 / 2
    # computer data
    # computer_graph = load_graph(NETWORK_URL)
    # computer_num_nodes = len(computer_graph.values())
    # computer_avg_connections = sum([len(i) for i in computer_graph.values()]) / computer_num_nodes

    # random undirected graph
    # random_udg = make_random_undirected_graph(num_nodes=computer_num_nodes,
    #                                           probability=computer_avg_connections / computer_num_nodes)
    # random_udg_connections = sum([len(i) for i in random_udg.values()]) / len(random_udg.values())

    # upa graph
    # upa_graph = ugraph_UPA(num_nodes=1239, m=2)
    # upa_graph_connections = sum([len(i) for i in upa_graph.values()]) / len(upa_graph.values())
    # print(upa_graph_connections)

    # resilience_list = []
    # for i in [computer_graph, random_udg, upa_graph]:
    #     resilience_list.append(compute_resilience(i, random_order(i)))
    # axes, figure = visualize_resilience(resilience_list)

    #
    # upa_graph = make_weighted_graph(num_nodes_full_connected=2, num_nodes_total=50)
    # print fast_targeted_order(upa_graph)

    ##########################################################33
    # Problem 3

    times_slow = []
    times_fast = []
    for n in range(10, 1000, 10):
        temp_upa_graph = ugraph_UPA(num_nodes=n, m=5)
        start1 = timeit.default_timer()
        targeted_order(temp_upa_graph)
        stop1 = timeit.default_timer()
        times_slow.append(stop1 - start1)

        start2 = timeit.default_timer()
        fast_targeted_order(temp_upa_graph)
        stop2 = timeit.default_timer()
        times_fast.append(stop2 - start2)
    run_times = [times_slow, times_fast]

    axes, figure = visualize_run_times(run_times)


    #######################################################################
    #Problem 4

    # resilience_list = []
    # for i in [computer_graph, random_udg, upa_graph]:
    #     resilience_list.append(compute_resilience(i, targeted_order(i)))
    # axes, figure = visualize_resilience(resilience_list, type_of_attack="targeted attack (regular algorithm)")


