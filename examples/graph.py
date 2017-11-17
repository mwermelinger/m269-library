"""Finding paths and tours between cities.

This undirected weighted graph is from Activity 5.1 of Unit 5 of M269.

The shortest distance between two cities can be computed in two different ways:

>>> start = "Luton"
>>> end = "Penzance"
>>> cities.weight(cities.shortest_path(start, end))
284
>>> cities.weighted_distance(start, end)
284

Although all cities are directly connected to each other,
the shortest path is not necessarily the direct path.

>>> cities.shortest_path(start, end)
['Luton', 'Nuneaton', 'Penzance']
"""

from lib.graph import Graph

cities = Graph()
cities.add_edge("Scunthorpe", "Bridlington", 31)
cities.add_edge("Scunthorpe", "Wick", 514)
cities.add_edge("Scunthorpe", "Bognor", 252)
cities.add_edge("Scunthorpe", "Nuneaton", 111)
cities.add_edge("Scunthorpe", "Luton", 117)
cities.add_edge("Scunthorpe", "Wrexham", 142)
cities.add_edge("Scunthorpe", "Penzance", 318)
cities.add_edge("Bridlington", "Luton", 142)
cities.add_edge("Bridlington", "Nuneaton", 115)
cities.add_edge("Bridlington", "Bognor", 209)
cities.add_edge("Bridlington", "Penzance", 426)
cities.add_edge("Bridlington", "Wrexham", 162)
cities.add_edge("Bridlington", "Wick", 512)
cities.add_edge("Luton", "Wick", 627)
cities.add_edge("Luton", "Bognor", 112)
cities.add_edge("Luton", "Wrexham", 151)
cities.add_edge("Luton", "Nuneaton", 65)
cities.add_edge("Luton", "Penzance", 320)
cities.add_edge("Nuneaton", "Wick", 566)
cities.add_edge("Nuneaton", "Bognor", 161)
cities.add_edge("Nuneaton", "Wrexham", 90)
cities.add_edge("Nuneaton", "Penzance", 219)
cities.add_edge("Bognor", "Wick", 720)
cities.add_edge("Bognor", "Wrexham", 243)
cities.add_edge("Bognor", "Penzance", 258)
cities.add_edge("Penzance", "Wick", 809)
cities.add_edge("Penzance", "Wrexham", 333)
cities.add_edge("Wick", "Wrexham", 508)


def print_graph(graph):
    """Print the number of nodes and edges, and each edge."""
    nodes = graph.nodes()
    edges = graph.weighted_edges()
    print("A graph with", len(nodes), "nodes and", len(edges), "edges")
    for (source, target, weight) in edges:
        print("Edge from", source, "to", target, "with weight", weight)


# If this file is imported, do nothing.
# If it is run as a script, execute the app.
if __name__ == "__main__":
    tour = cities.best_tour()
    print(tour, "\nis a shortest tour of length", cities.weight(tour))
    print()
    print("A minimum spanning tree:")
    print_graph(cities.minimum_spanning_tree("Luton"))
    print()
    print("Type two cities to get the shortest path between them.")
    print("To end the program, just type ENTER.")
    start = input("Start city: ")
    while start:
        end = input("End city: ")
        if cities.has_node(start) and cities.has_node(end):
            path = cities.shortest_path(start, end)
            print(path, "is a shortest path of length", cities.weight(path))
        else:
            print("At least one of the cities doesn't exist.")
        start = input("Start city: ")
