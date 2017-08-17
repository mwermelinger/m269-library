"""Examples of undirected graphs"""

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


# Graph from [Section 7.20](http://www.interactivepython.org/courselib/static/pythonds/Graphs/DijkstrasAlgorithm.html)
# of Miller & Ranum's book
# _Problem Solving with Algorithms and Data Structures using Python_

graph = Graph()
graph.add_edge('u', 'v', 2)
graph.add_edge('u', 'x', 1)
graph.add_edge('u', 'w', 5)
graph.add_edge('v', 'x', 2)
graph.add_edge('v', 'w', 3)
graph.add_edge('x', 'w', 3)
graph.add_edge('x', 'y', 1)
graph.add_edge('w', 'y', 1)
graph.add_edge('w', 'z', 5)
graph.add_edge('y', 'z', 1)
print_graph(graph)
print('DFS from u:', graph.visited_dfs('u'))
print('DFS from z:', graph.visited_dfs('z'))
print('BFS from u:', graph.visited_bfs('u'))
print('BFS from z:', graph.visited_bfs('z'))

graph.remove_node('v')
print('Removed node v')
print_graph(graph)
print('DFS from u:', graph.visited_dfs('u'))
print('DFS from z:', graph.visited_dfs('z'))
print('BFS from u:', graph.visited_bfs('u'))
print('BFS from z:', graph.visited_bfs('z'))

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
