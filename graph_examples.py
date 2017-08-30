"""Examples of undirected graphs."""

from graph import Graph


def print_graph(graph):
    """Print the number of nodes and edges, and each edge."""
    nodes = graph.nodes()
    edges = graph.weighted_edges()
    print('A graph with', len(nodes), 'nodes and', len(edges), 'edges')
    for (source, target, weight) in edges:
        print('Edge from', source, 'to', target, 'with weight', weight)


def test(name, actual, expected):
    """Check that the actual result is one of the expected."""
    if actual in expected:
        print('OK:', name, '=', actual)
    else:
        print('FAILED:', name, '=', actual)


def test_shortest(graph, start, end):
    """Check that the shortest distance, computed twice, is the same."""
    path = graph.shortest_path(start, end)
    distance1 = graph.weight(path)
    distance2 = graph.weighted_distance(start, end)
    print('Shortest path', start, '->', end, 'of length', distance1, ':')
    print(path)
    if distance1 != distance2:
        print('FAILED: different weighted_distance', distance2)


# Graph from Section 7.20 of Miller and Ranum's
# [book](http://interactivepython.org/runestone/static/pythonds/index.html)
# _Problem Solving with Algorithms and Data Structures using Python_

example = Graph()
example.add_edge('u', 'v', 2)
example.add_edge('u', 'x', 1)
example.add_edge('u', 'w', 5)
example.add_edge('v', 'x', 2)
example.add_edge('v', 'w', 3)
example.add_edge('x', 'w', 3)
example.add_edge('x', 'y', 1)
example.add_edge('w', 'y', 1)
example.add_edge('w', 'z', 5)
example.add_edge('y', 'z', 1)
print_graph(example)
print('DFS from u:', example.visited_dfs('u'))
print('DFS from z:', example.visited_dfs('z'))
print('BFS from u:', example.visited_bfs('u'))
print('BFS from z:', example.visited_bfs('z'))
print('from u to z:', example.unweighted_distance('u', 'z'), 'hops')

test('distance u to w', example.weighted_distance('u', 'w'), [3])
test('path u to w', example.shortest_path('u', 'w'), [['u', 'x', 'y', 'w']])
print('MST from u:')
print_graph(example.minimum_spanning_tree('u'))

example.remove_node('v')
print('Removed node v')
print_graph(example)
print('DFS from u:', example.visited_dfs('u'))
print('DFS from z:', example.visited_dfs('z'))
print('BFS from u:', example.visited_bfs('u'))
print('BFS from z:', example.visited_bfs('z'))
print('MST from u:')
print_graph(example.minimum_spanning_tree('u'))

example.remove_node('w')
print('Removed node w')
print('from u to z:', example.unweighted_distance('u', 'z'), 'hops')
print('from u to w:', example.unweighted_distance('u', 'w'), 'hops')

print('topological sort:', example.topological_sort())

# Graph from Python activity 5.1 from Unit 5 of M269

cities = Graph()
cities.add_edge('Scunthorpe', 'Bridlington', 31)
cities.add_edge('Scunthorpe', 'Wick', 514)
cities.add_edge('Scunthorpe', 'Bognor', 252)
cities.add_edge('Scunthorpe', 'Nuneaton', 111)
cities.add_edge('Scunthorpe', 'Luton', 117)
cities.add_edge('Scunthorpe', 'Wrexham', 142)
cities.add_edge('Scunthorpe', 'Penzance', 318)
cities.add_edge('Bridlington', 'Luton', 142)
cities.add_edge('Bridlington', 'Nuneaton', 115)
cities.add_edge('Bridlington', 'Bognor', 209)
cities.add_edge('Bridlington', 'Penzance', 426)
cities.add_edge('Bridlington', 'Wrexham', 162)
cities.add_edge('Bridlington', 'Wick', 512)
cities.add_edge('Luton', 'Wick', 627)
cities.add_edge('Luton', 'Bognor', 112)
cities.add_edge('Luton', 'Wrexham', 151)
cities.add_edge('Luton', 'Nuneaton', 65)
cities.add_edge('Luton', 'Penzance', 320)
cities.add_edge('Nuneaton', 'Wick', 566)
cities.add_edge('Nuneaton', 'Bognor', 161)
cities.add_edge('Nuneaton', 'Wrexham', 90)
cities.add_edge('Nuneaton', 'Penzance', 219)
cities.add_edge('Bognor', 'Wick', 720)
cities.add_edge('Bognor', 'Wrexham', 243)
cities.add_edge('Bognor', 'Penzance', 258)
cities.add_edge('Penzance', 'Wick', 809)
cities.add_edge('Penzance', 'Wrexham', 333)
cities.add_edge('Wick', 'Wrexham', 508)
print('DFS from Wick:', cities.visited_dfs('Wick'))
print('BFS from Wick:', cities.visited_bfs('Wick'))
tour = cities.best_tour()
print(tour, 'is a shortest tour of length', cities.weight(tour))

test_shortest(cities, 'Wick', 'Luton')
test_shortest(cities, 'Bridlington', 'Penzance')
test_shortest(cities, 'Bridlington', 'Penance')
test_shortest(cities, 'Wick', 'Wick')

print_graph(cities.minimum_spanning_tree('Luton'))
