class DirectedGraph:
    """Implements a directed graph (digraph).

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
    # In the `node_info` dictionary, keys are nodes, and values are
    # dictionaries where the algorithms store information about the nodes,
    # e.g. which nodes have been visited.
    # In the `edge_info` dictionary, keys are nodes, and values are
    # dictionaries where the keys are nodes and the values are weights.
    #
    # For example, a digraph with two nodes `start` and `end` and
    # a single edge between them of weight 3, is initially represented as
    # `node_info = {'start': {}, 'end': {}}`
    # and
    # `edge_info = {'start': {'end': 3}}`.
    # After running an algorithm to visit the nodes, the `node_info` will be
    # {'start': {'seen': True}, 'end': {'seen': True}}`.

    def __init__(self):
        """Initialise the empty digraph."""
        self.node_info = dict()
        self.edge_info = dict()

    # Inspectors
    # ----------

    def has_node(self, node):
        """Return True if the graph contains the node, otherwise False."""
        return node in self.node_info

    def has_edge(self, source, target):
        """Check if the graph has a directed edge from source to target.

        Return True if it has, otherwise False.
        Assume source and target are nodes in the graph.
        """
        assert self.has_node(source)
        assert self.has_node(target)
        return target in self.edge_info[source]

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
            total = total + self.edge_info[this_node][next_node]
        return total

    def nodes(self):
        """Return the set of all nodes in the graph."""
        return set(self.node_info.keys())

    def unweighted_edges(self):
        """Return the set of all edges in the graph, without weights.

        An edge is a tuple (source, target).
        """
        the_edges = set()
        for source in self.edge_info:
            for target in self.edge_info[source]:
                the_edges.add((source, target))
        return the_edges

    def weighted_edges(self):
        """Return the set of all edges in the graph, with weights.

        An edge is a tuple (source, target, weight).
        """
        the_edges = set()
        for source in self.edge_info:
            for target in self.edge_info[source]:
                edge = (source, target, self.weight([source, target]))
                the_edges.add(edge)
        return the_edges

    def neighbours(self, node):
        """Return the set of neighbours of node.

        Assume the graph has node.
        """
        assert self.has_node(node)
        return set(self.edge_info[node].keys())

    # Breadth-first search
    # --------------------
    # Breadth-first search starts at a given node and first visits
    # all its neighbours, then all the neighbours' neighbours, etc.

    def visited_bfs(self, start):
        """Do a breadth-first search of the graph, from the start node.

        Return a list of nodes in visited order, the first being start.
        Assume the graph has the start node.
        """
        # Initialise the list to be returned.
        visited = []
        # Keep the nodes yet to visit in another list, used as a queue.
        # Initially, only the start node is to be visited.
        to_visit = [start]
        # Mark all nodes except the start node as unexplored.
        for node in self.node_info:
            self.node_info[node]['seen'] = False
        self.node_info[start]['seen'] = True
        # While there are nodes to be visited:
        while to_visit != []:
            # Visit the next node at the front of the queue.
            next_node = to_visit.pop(0)
            visited.append(next_node)
            # Look at its neighbours.
            for neighbour in self.neighbours(next_node):
                # Put unexplored nodes at the back of the queue
                # and mark them as explored.
                if not self.node_info[neighbour]['seen']:
                    to_visit.append(neighbour)
                    self.node_info[neighbour]['seen'] = True
        return visited

    # Depth-first search
    # ------------------

    def visited_dfs(self, start):
        """Do a depth-first search of the graph, from the start node.

        Return a list of nodes in visited order, the first being start.
        Assume the start node exists.
        """
        assert self.has_node(start)
        visited = []
        to_visit = [start]
        for node in self.node_info:
            self.node_info[node]['seen'] = False
        self.node_info[start]['seen'] = True
        while to_visit != []:
            next_node = to_visit.pop()
            visited.append(next_node)
            for neighbour in self.neighbours(next_node):
                if not self.node_info[neighbour]['seen']:
                    to_visit.append(neighbour)
                    self.node_info[neighbour]['seen'] = True
        return visited

    # Modifiers
    # ---------

    def add_node(self, node):
        """Add node to the graph.

        Do nothing if the graph already has node.
        Assume the node is of a hashable type.
        """
        if not self.has_node(node):
            self.edge_info[node] = dict()
            self.node_info[node] = dict()

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
        self.edge_info[source][target] = weight

    def remove_edge(self, source, target):
        """Remove the edge from source to target from the graph.

        Do nothing if the edge doesn't exist.
        Assume the graph has both nodes.
        """
        assert self.has_node(source)
        assert self.has_node(target)
        if target in self.edge_info[source]:
            del self.edge_info[source][target]

    def remove_node(self, node):
        """Remove the node and its incident edges from the graph.

        Assume the node exists.
        """
        assert self.has_node(node)
        for source in self.nodes():
            self.remove_edge(source, node)
        for target in self.neighbours(node):
            self.remove_edge(node, target)
        del self.edge_info[node]
        del self.node_info[node]


# Exercises
# ---------
# - Add a method to:
#   - compute the **size** of a graph, i.e. the number edges.
#   - compute the **order** of a graph, i.e. the number of nodes.
#   - check if a given list of nodes is a path in the graph.
#   - check if a graph is unweighted.
