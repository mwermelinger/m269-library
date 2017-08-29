"""An implementation of weighted directed graphs."""

# This file is part of the [M269 Library](http://tiny.cc/m269-library).

from queue import Queue  # for the breadth-first search
from stack import Stack  # for the depth-first search


class DirectedGraph:
    """Implement a directed graph (digraph).

    Each node must be a hashable value:
    a number, string, tuple of hashable values, etc.
    Each edge has a direction, i.e. it goes **from** a node **to** another.
    The two nodes must be different.
    Each edge has a weight, which must be a positive number.
    If all weights are the same, the graph is effectively unweighted.
    """

    # Representation
    # --------------
    # The digraph is stored as two dictionaries-of-dictionaries.
    # In the `_nodes` dictionary, keys are nodes, and values are
    # dictionaries where the algorithms store information about the nodes,
    # e.g. which nodes have been visited.
    # In the `_edges` dictionary, keys are nodes, and values are
    # dictionaries where the keys are nodes and the values are weights.
    #
    # For example, a digraph with two nodes `start` and `end` and
    # a single edge between them of weight 3 is represented as
    # `_nodes = {'start': {}, 'end': {}}`
    # and
    # `_edges = {'start': {'end': 3}}`.
    # After running an algorithm to visit the nodes, `_nodes` may be
    # {'start': {'seen': True}, 'end': {'seen': True}}`.

    def __init__(self):
        """Initialise the empty digraph."""
        self._nodes = dict()
        self._edges = dict()

    # Inspectors
    # ----------

    def has_node(self, node):
        """Return True if the graph contains the node, otherwise False."""
        return node in self._nodes

    def has_edge(self, source, target):
        """Check if the graph has a directed edge from source to target.

        Return False if the edge or either node don't exist, otherwise True.
        """
        return self.has_node(source) and target in self._edges[source]

    def weight(self, path):
        """Return the total weight of the path.

        A path is a list of at least two nodes of the graph [n1, n2, ...]
        such that n1-n2, n2-n3, etc. are edges in the graph.
        Assume the path is valid.
        """
        assert len(path) > 1
        total = 0
        for current in range(0, len(path) - 1):
            this_node = path[current]
            next_node = path[current + 1]
            assert self.has_edge(this_node, next_node)
            total = total + self._edges[this_node][next_node]
        return total

    def nodes(self):
        """Return the set of all nodes in the graph."""
        return set(self._nodes.keys())

    def unweighted_edges(self):
        """Return the set of all edges in the graph, without weights.

        An edge is a tuple (source, target).
        """
        the_edges = set()
        for source in self._edges:
            for target in self._edges[source]:
                the_edges.add((source, target))
        return the_edges

    def weighted_edges(self):
        """Return the set of all edges in the graph, with weights.

        An edge is a tuple (source, target, weight).
        """
        the_edges = set()
        for source in self._edges:
            for target in self._edges[source]:
                weight = self._edges[source][target]
                the_edges.add((source, target, weight))
        return the_edges

    def neighbours(self, node):
        """Return the set of neighbours of node.

        Assume the graph has the node.
        """
        assert self.has_node(node)
        return set(self._edges[node].keys())

    # Breadth-first search
    # --------------------
    # Breadth-first search starts at a given node and first visits
    # all its neighbours, then all the neighbours' neighbours, etc.

    def visited_bfs(self, start):
        """Do a breadth-first search of the graph, from the start node.

        Return a list of nodes in visited order, the first being start.
        Assume the start node exists.
        """
        assert self.has_node(start)
        # Initialise the list to be returned.
        visited = []
        # Keep the nodes yet to visit in another list, used as a queue.
        # Initially, only the start node is to be visited.
        to_visit = Queue()
        to_visit.enqueue(start)
        # Mark all nodes except the start node as unexplored.
        for node in self._nodes:
            self._nodes[node]['seen'] = False
        self._nodes[start]['seen'] = True
        # While there are nodes to be visited:
        while not to_visit.is_empty():
            # Visit the next node at the front of the queue.
            next_node = to_visit.dequeue()
            visited.append(next_node)
            # Look at its neighbours.
            for neighbour in self.neighbours(next_node):
                # Put unexplored nodes at the back of the queue
                # and mark them as explored.
                if not self._nodes[neighbour]['seen']:
                    to_visit.enqueue(neighbour)
                    self._nodes[neighbour]['seen'] = True
        return visited

    # Breadth-first search can be used to find the smallest number
    # of 'hops' to go from one node to another, because it first
    # visits all nodes 1 hop away, then those 2 hops away, etc.

    def unweighted_distance(self, start, end):
        """Return the smallest number of edges to go from `start` to `end`.

        Return infinity if there is no path from `start` to `end`.
        Assume the graph has the start node.
        """
        # Like breadth-first search but keep each node's distance from `start`.
        assert self.has_node(start)
        infinity = float('infinity')
        to_visit = Queue()
        to_visit.enqueue(start)
        for node in self._nodes:
            self._nodes[node]['distance'] = infinity
        self._nodes[start]['distance'] = 0
        while not to_visit.is_empty():
            next_node = to_visit.dequeue()
            distance = self._nodes[next_node]['distance']
            if next_node == end:
                return distance
            for neighbour in self.neighbours(next_node):
                if self._nodes[neighbour]['distance'] == infinity:
                    to_visit.enqueue(neighbour)
                    self._nodes[neighbour]['distance'] = distance + 1
        return infinity

    # Depth-first search
    # ------------------

    def visited_dfs(self, start):
        """Do a depth-first search of the graph, from the start node.

        Return a list of nodes in visited order, the first being start.
        Assume the start node exists.
        """
        assert self.has_node(start)
        # Use the same algorithm, but keep nodes to visit in a stack.
        visited = []
        to_visit = Stack()
        to_visit.push(start)
        for node in self._nodes:
            self._nodes[node]['seen'] = False
        self._nodes[start]['seen'] = True
        while not to_visit.is_empty():
            next_node = to_visit.pop()
            visited.append(next_node)
            for neighbour in self.neighbours(next_node):
                if not self._nodes[neighbour]['seen']:
                    to_visit.push(neighbour)
                    self._nodes[neighbour]['seen'] = True
        return visited

    def topological_sort(self):
        """Return a list of nodes, in topological order.

        Return the empty list if the graph is cyclic.
        """
        sort = []
        # Initially, all nodes have 0 incoming edges and can be visited.
        to_visit = self.nodes()
        for node in to_visit:
            self._nodes[node]['incoming'] = 0
        # For each edge, its target has 1 more incoming edge,
        # and can't be yet visited (the source must be visited first).
        # pylint: disable=unused-variable
        for (source, target) in self.unweighted_edges():
            to_visit.discard(target)
            self._nodes[target]['incoming'] += 1
        # While there are nodes to visit,
        while to_visit:
            # visit any of them,
            node = to_visit.pop()
            sort.append(node)
            # and virtually remove it from the graph, by
            # decrementing its neighbours' incoming edges.
            for neighbour in self.neighbours(node):
                self._nodes[neighbour]['incoming'] -= 1
                # If a node has no incoming edges left,
                # all its predecessors were visited and 'removed',
                # hence it can be visited.
                if self._nodes[neighbour]['incoming'] == 0:
                    to_visit.add(neighbour)
        return sort

    # Modifiers
    # ---------

    def add_node(self, node):
        """Add the node to the graph.

        Do nothing if the graph already has the node.
        Assume the node is of a hashable type.
        """
        if not self.has_node(node):
            self._edges[node] = dict()
            self._nodes[node] = dict()

    def add_edge(self, source, target, weight=1):
        """Add a directed edge from source to target with the given weight.

        Replace the weight value if the edge already exists.
        Add any node that doesn't exist.
        Assume the two nodes are different.
        Assume the weight is a positive number.
        Assume the nodes are of a hashable type.
        """
        assert source != target
        assert weight > 0
        self.add_node(source)
        self.add_node(target)
        self._edges[source][target] = weight

    def remove_edge(self, source, target):
        """Remove the edge from source to target from the graph.

        Do nothing if the edge doesn't exist.
        """
        if self.has_edge(source, target):
            del self._edges[source][target]

    def remove_node(self, node):
        """Remove the node and its edges from the graph.

        Do nothing if the node doesn't exist.
        """
        if not self.has_node(node):
            return
        for source in self.nodes():
            self.remove_edge(source, node)
        del self._edges[node]
        del self._nodes[node]


# Exercises
# ---------
# - Add a method to:
#   - compute the **size** of a graph, i.e. the number of edges.
#   - compute the **order** of a graph, i.e. the number of nodes.
#   - check if a given list of nodes is a path in the graph.
#   - check if a graph is unweighted.
