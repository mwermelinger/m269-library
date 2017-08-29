"""Examples of directed graphs."""

from digraph import DirectedGraph


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


# Food web
# --------
# This is a directed, acyclic, unweighted graph.
# Nodes are species and an edge from A to B states that A is eaten by B.

food_web = DirectedGraph()
food_web.add_edge('rabbit', 'fox')
food_web.add_edge('grass', 'rabbit')
food_web.add_edge('mouse', 'fox')
food_web.add_edge('grass', 'mouse')
print_graph(food_web)

# There are two depth-first traversals from 'grass'
df1 = ['grass', 'rabbit', 'fox', 'mouse']
df2 = ['grass', 'mouse', 'fox', 'rabbit']
test('dfs from grass', food_web.visited_dfs('grass'), [df1, df2])
# but only one from 'mouse'
df1 = ['mouse', 'fox']
test('dfs from mouse', food_web.visited_dfs('mouse'), [df1])
# or from 'fox'.
test('dfs from fox', food_web.visited_dfs('fox'), [['fox']])

# There are two breadth-first traversals from 'grass'
bf1 = ['grass', 'rabbit', 'mouse', 'fox']
bf2 = ['grass', 'mouse', 'rabbit', 'fox']
test('bfs from grass', food_web.visited_bfs('grass'), [bf1, bf2])
# but only one from 'mouse'
bf1 = ['mouse', 'fox']
test('bfs from mouse', food_web.visited_bfs('mouse'), [bf1])
# or from 'fox'.
test('bfs from fox', food_web.visited_bfs('fox'), [['fox']])

test('from fox to fox', food_web.unweighted_distance('fox', 'fox'), [0])
test('from grass to fox', food_web.unweighted_distance('grass', 'fox'), [2])
test('from fox to grass', food_web.unweighted_distance('fox', 'grass'),
     [float('infinity')])

# Recipe
# ------
# Graph from Section 7.20 of Miller and Ranum's
# [book](http://interactivepython.org/runestone/static/pythonds/index.html)
# _Problem Solving with Algorithms and Data Structures using Python_

recipe = DirectedGraph()
recipe.add_edge('3/4 cup milk', '1 cup mix')
recipe.add_edge('1 egg', '1 cup mix')
recipe.add_edge('1 Tbl Oil', '1 cup mix')
recipe.add_edge('1 cup mix', 'pour 1/4 cup')
recipe.add_edge('1 cup mix', 'heat syrup')
recipe.add_edge('heat syrup', 'eat')
recipe.add_edge('heat griddle', 'pour 1/4 cup')
recipe.add_edge('pour 1/4 cup', 'turn when bubbly')
recipe.add_edge('turn when bubbly', 'eat')

print('Order of steps:', recipe.topological_sort())
