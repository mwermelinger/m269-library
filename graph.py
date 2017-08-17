from digraph import DirectedGraph
from itertools import permutations  # needed for best_tour


class Graph (DirectedGraph):
    """Implements an undirected graph.

    Each node must be a hashable value:
    a number, a string, a tuple of hashable values, etc.
    Each edge must be between two different nodes.
    Each edge has a weight, which must be a positive number.
    If all weights are the same, the graph is effectively unweighted.
    """

    # Representation
    # --------------
    # An undirected graph is a special case of a digraph,
    # in which for each directed edge the opposite edge also exists.
    # This class therefore inherits the representation and
    # most of the methods from the `DirectedGraph` class.

    # Creator
    # -------
    # Inherited from `DirectedGraph`.

    # Inspectors
    # ----------
    # Mostly inherited from `DirectedGraph`.

    # The following only changes the docstring.
    def has_edge(self, node1, node2):
        """Check if there's an edge between the two nodes.

        Return True if there is, otherwise False.
        Assume both nodes exist.
        """
        assert self.has_node(node1) and self.has_node(node2)
        return node2 in self.edge_info[node1]

    # The following were changed to not generate duplicate edges.
    def weighted_edges(self):
        """Return the set of all edges in self, with weights.

        An edge is a tuple (node1, node2, weight).
        The returned set doesn't duplicate edges, i.e. only one of
        (node1, node2, weight) and (node2, node1, weight) is included.
        """
        the_edges = set()
        for source in self.edge_info:
            for target in self.edge_info[source]:
                weight = self.weight([source, target])
                if (target, source, weight) not in the_edges:
                    the_edges.add((source, target, weight))
        return the_edges

    def unweighted_edges(self):
        """Return the set of all edges in self, without weights.

        An edge is a tuple (node1, node2).
        The returned set doesn't duplicate edges, i.e. only one of
        (node1, node2) and (node2, node1) is included.
        """
        the_edges = set()
        for source in self.edge_info:
            for target in self.edge_info[source]:
                if (target, source) not in the_edges:
                    the_edges.add((source, target))
        return the_edges

    # The Travelling Salesman Problem
    # -------------------------------
    # The problem consists in finding a best tour in
    # a complete weighted undirected graph.
    # A complete graph has an edge between any pair of nodes.
    # A tour is a path that starts and ends in the same node
    # and goes through all the other nodes.
    # The best tours (there may be several) have the lowest total weight.
    # Weights usually represent distances or costs,
    # so the best tours are the shortest or cheapest ones.

    def best_tour(self):
        """Return a best tour of the graph.

        Assume the graph is complete.
        A tour is a list with all the graph's nodes, in the order visited,
        and the first and last nodes are the same.
        A best tour has the lowest total weight.
        Use a brute-force algorithm (only works for very small graphs).
        """
        # Mark that no tour has been found yet.
        tour_found = None
        lowest_total = float('infinity')
        # Go through all possible orderings of the nodes.
        for permutation in permutations(self.nodes()):
            # A tour is a permutation with the start node at the end.
            # First convert the permutation from a tuple to a list.
            tour = list(permutation)
            tour.append(tour[0])
            # Compute the tour's weight. Update the best found, if the case.
            total = self.weight(tour)
            if tour_found is None or total < lowest_total:
                lowest_total = total
                tour_found = tour
        return tour_found

    # Modifiers
    # ---------
    # `add_node` and `remove_node` inherited from `Digraph`.

    def add_edge(self, this_node, that_node, weight=1):
        """Add an edge between the two nodes with the given weight.

        Replace the weight value if the edge already exists.
        Assume the nodes are of a hashable type and different.
        Assume the weight is a positive number.
        """
        assert this_node != that_node
        assert weight > 0
        self.add_node(this_node)
        self.add_node(that_node)
        self.edge_info[this_node][that_node] = weight
        self.edge_info[that_node][this_node] = weight

    def remove_edge(self, node1, node2):
        """Remove the edge between the nodes from the graph.

        Do nothing if the edge doesn't exist.
        Assume the graph has both nodes.
        """
        assert self.has_node(node1)
        assert self.has_node(node2)
        if self.has_edge(node1, node2):
            del self.edge_info[node1][node2]
            del self.edge_info[node2][node1]

# Exercises
# ---------
# - Redo all exercises for directed graphs that need to be adapted to
#   or can be made more efficient for undirected graphs.
# - Add a method that checks if a graph is complete.
