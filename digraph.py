"""A pedagogical implementation of directed graphs.

A directed graph is a possibly empty collection of nodes and edges.
Each edge goes *from* one node (called the **source** node)
*to* the same or a different node (the **target** node).
If the source and target nodes are the same, the edge is called a **loop**.
"""

# Representation
# --------------
# A graph is represented by a dictionary of adjacency lists, i.e.
# each node is mapped to the list of its neighbours.
# For example, the graph 1 <-> 2 -> 3 is represented as
# `{ 1: [2], 2: [1,3], 3: []}` or as `{ 1: [2], 2: [3,1], 3: []}`
# because the order of nodes in the neighbour list doesn't matter.

# Due to the use of dictionaries, each node must be of a hashable type:
# it can be a number, a string (with the label of the node) or
# a tuple with more information about the node.

# Creator
# -------


def empty():
    """Return the empty graph."""
    return dict()


# Modifiers
# ----------


def add_node(graph, node):
    """If `graph` hasn't `node`, add it, otherwise do nothing.
    Raise TypeError if `node` is not of a hashable type.
    """
    if node not in graph:
        # The new node has no neighbours.
        graph[node] = []


def add_edge(graph, source, target):
    """Add to `graph` an edge from `source` to `target`.
    Do nothing if the edge already exists.
    Add `source` and `target` if they don't exist in `graph`.
    Raise TypeError if `source` or `target` are not of a hashable type.
    """
    add_node(graph, source)
    add_node(graph, target)
    if target not in graph[source]:
        graph[source].append(target)


# Inspectors
# ----------


def nodes(graph):
    """Return the set of nodes in `graph`."""
    # Use the built-in dictonary method to obtain the keys.
    return set(graph.keys())


def has_node(graph, node):
    """Return True if `graph` has `node`, otherwise False."""
    # Use the Python way of checking if `node` is a key of `graph`.
    return node in graph


def neighbours(graph, node):
    """Return the set of neighbours of `node` in `graph`.
    Raise ValueError if `graph` hasn't `node`.
    """
    # If this function returned directly the neighbours list,
    # the client could change it directly without using `add_edge()`
    # and thus 'break' the graph by adding neighbours that are not nodes.
    if node not in graph:
        raise ValueError("graph must have the given node")
    return set(graph[node])


# The following functions are independent of how the graph is represented.


def bfs(graph, node):
    """Do a breadth-first search of `graph`, starting from `node`.
    Return a list of nodes in visited order, the first being `node`.
    Raise ValueError if `graph` hasn't `node`.
    """
    visited = []
    # Keep the nodes yet to visit in a queue.
    # Initially, only the start node is to be visited.
    to_visit = [node]
    # While there are nodes to be visited:
    while to_visit != []:
        # Visit the next node at the front of the queue.
        next_node = to_visit.pop(0)
        visited.append(next_node)
        # Explore its neighbours.
        for neighbour in neighbours(graph, next_node):
            # Put nodes not previously seen at the back of the queue.
            if neighbour not in visited + to_visit:
                to_visit.append(neighbour)
    return visited


def dfs(graph, node):
    """Do a depth-first search of `graph`, starting from `node`.
    Return a list of nodes in visited order, the first being `node`.
    Raise ValueError if `graph` hasn't `node`.
    """
    # Same algorithm as `bfs()`, but `to_visit` is a stack, not a queue.
    visited = []
    to_visit = [node]
    while to_visit != []:
        next_node = to_visit.pop()
        visited.append(next_node)
        for neighbour in neighbours(graph, next_node):
            if neighbour not in visited + to_visit:
                to_visit.append(neighbour)
    return visited


# Tests
# -----
# Run tests if this file is executed, instead of imported.
if __name__ == "__main__":
    graph = empty()
    if nodes(graph) != set():
        print("nodes(", graph, ") is", nodes(graph), "instead of empty set.")

    if has_node(graph, 5):
        print("has_node(", graph, ", 5) is True instead of False.")

    try:
        add_node(graph, [])
        print("adding [] has not raised TypeError")
    except TypeError:
        pass
    except Exception as e:
        print("adding [] raised", e, "instead of TypeError")

    add_edge(graph, 1, 2)
    add_edge(graph, 1, 3)
    add_edge(graph, 2, 3)
    add_edge(graph, 2, 4)
    add_edge(graph, 3, 1)
    try:
        bfs(graph, 5)
        print("bfs(", graph, ", 5) didn't raise ValueError")
    except ValueError:
        pass
    except Exception as e:
        print("bfs(", graph, ", 5) raised", e, "instead of ValueError")

    actual = bfs(graph, 1)
    expected = [1, 2, 3, 4]
    if actual != expected:
        print("bfs(", graph, ", 1) is", actual, "instead of", expected)

    actual = dfs(graph, 1)
    expected = [1, 3, 2, 4]
    if actual != expected:
        print("dfs(", graph, ", 1) is", actual, "instead of", expected)

    actual = bfs(graph, 2)
    expected = [2, 3, 4, 1]
    if actual != expected:
        print("bfs(", graph, ", 2) is", actual, "instead of", expected)

    actual = dfs(graph, 2)
    expected = [2, 4, 3, 1]
    if actual != expected:
        print("dfs(", graph, ", 2) is", actual, "instead of", expected)

    actual = bfs(graph, 3)
    expected = dfs(graph, 3)
    if actual != expected:
        print("bfs(", graph, ", 3) is", actual, "instead of", expected)


# Exercises
# ---------

# - Write a function that returns the set of all edges in a graph.
#   Decide how to represent each edge.
# - Write a function that checks if the graph has at least one loop.
