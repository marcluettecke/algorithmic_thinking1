from week2.project1 import make_complete_graph

"""
Provided code for application portion of module 2

Helper class for implementing efficient version
of UPA algorithm
"""

import random


class UPATrial:
    """
    Simple class to encapsulate optimizated trials for the UPA algorithm

    Maintains a list of node numbers with multiple instance of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities

    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a UPATrial object corresponding to a
        complete graph with num_nodes nodes

        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]

    def run_trial(self, num_nodes):
        """
        Conduct num_nodes trials using by applying random.choice()
        to the list of node numbers

        Updates the list of node numbers so that each node number
        appears in correct ratio

        Returns:
        Set of nodes
        """

        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for _ in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))

        # update the list of node numbers so that each node number
        # appears in the correct ratio

        self._node_numbers.append(self._num_nodes)
        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))

        # update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors


def ugraph_UPA(num_nodes, m):
    """

    Args:
        num_nodes:
        m:

    Returns:

    """
    ugraph = make_complete_graph(m)
    ugraph_ge = UPATrial(m)
    for item in range(m, num_nodes):
        ugraph[item] = ugraph_ge.run_trial(m)

    # make sure the edge is bothway
    for key, values in ugraph.items():
        for value in values:
            ugraph[value].add(key)

    return ugraph

def find_m():
    """

    Returns:

    """
    NODES = 1239
    EDGES = 3112
    for m in range(1, 6):
        ugraph = ugraph_UPA(NODES, m)
        num_edge = sum([len(value) for value in ugraph.values()])
        print("m: %d, the difference: %d" %(m, num_edge-EDGES))
    #m = 2


if __name__ == '__main__':
    dpa_instance = UPATrial(num_nodes=5)
    # print dpa_instance._node_numbers
    test = dpa_instance.run_trial(num_nodes=4)
    # print(test)
    # print(test)
    # print(dpa_instance._node_numbers)
