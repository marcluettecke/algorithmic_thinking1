"""
Functions to determine the common undirected graph functionalities, such as BFS, connected components and graph
resilience
"""
# common imports
from collections import deque
import random

GRAPH = {
    1: {3},
    2: {3},
    3: {1, 2, 4, 8},
    4: {3},
    5: {6, 7},
    6: {5},
    7: {5},
    8: {3}
}


def bfs_visited(ugraph, start):
    """
    Implementation of the BFS visited algorithm, which returns a set of all nodes visited by the algorithm
    Args:
        ugraph: undirecte graph in dictionary format {node: neighbors}
        start: start node from which the algorithm parses through the graph

    Returns:
        Set of all visited nodes from the start node
    """
    queue = deque()
    visited = {start}
    queue.append(start)

    while queue:
        current_element = queue.pop()
        for neighbor in ugraph[current_element]:
            if neighbor not in visited:
                visited = visited.union({neighbor})
                queue.append(neighbor)
    return visited


def cc_visited(ugraph):
    """
    Method to find the connected components in an undirected graph.
    Args:
        ugraph: undirecte graph in dictionary format {node: neighbors}

    Returns:
        List of sets where each set corresponds to the connected components in a graph.
    """
    remaining_nodes = set(ugraph.keys())
    result_list = []

    while remaining_nodes != set():
        random_entry = random.sample(remaining_nodes, 1)[0]
        visited = bfs_visited(ugraph=ugraph, start=random_entry)
        if visited == set():
            continue
        remaining_nodes = remaining_nodes - visited
        result_list.append(visited)
    return result_list


def largest_cc_size(ugraph):
    """
    Function to return the largest connected component size of an undirected graph.
    Args:
        ugraph: undirecte graph in dictionary format {node: neighbors}

    Returns:
        integer of largest connected component in undirected graph.
    """
    cc_visited_list = cc_visited(ugraph)
    try:
        max_integer = max([len(i) for i in cc_visited_list])
    except ValueError:
        max_integer = 0
    return max_integer


def compute_resilience(ugraph, attack_order):
    """
    Function to compute reslience of a graph by continuously removing nodes and computing the resulting largest
    connected component still remaining.
    Args:
        ugraph: undirecte graph in dictionary format {node: neighbors}
        attack_order: lit of nodes which are continuously turned off (not individually but adding one another)

    Returns:
        List of largest components of size k+1 (k being the size of the attack_order), first entry is before any
        attacks, subsequent entries after removing node at index k in attack order.
    """
    components_list = [largest_cc_size(ugraph)]
    configured_graph = ugraph
    # print configured_graph[5]

    for node in attack_order:
        # delete edge
        del configured_graph[node]
        for value in configured_graph.values():
            if node in value:
                # deletes all connections to the given edge IN PLACE
                value.remove(node)
        components_list.append(largest_cc_size(configured_graph))
    return components_list


if __name__ == '__main__':
    # print bfs_visited(GRAPH, 5)
    print compute_resilience(GRAPH, [5, 4, 3])
