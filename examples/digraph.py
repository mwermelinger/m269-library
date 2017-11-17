"""Using a directed graph to represent the steps in a recipe.

The example is from Section 7.17 of Miller and Ranum's book
'Problem Solving with Algorithms and Data Structures using Python'
(http://interactivepython.org/runestone/static/pythonds/index.html).

Depth- or breadth-first traversal tells us which steps depend on a given one.

>>> set(recipe.visited_dfs('1 egg')) == set(recipe.visited_bfs('1 egg'))
True

The distance between an ingredient and eating is a lower bound
on the number of sequential (i.e. non-parallel) steps needed
to execute the recipe. For unweighted graphs, the distance 
can be computed in two different ways.

>>> recipe.unweighted_distance('1 egg', 'eat')
3
>>> recipe.weight(recipe.shortest_path('1 egg', 'eat'))
3
"""

from lib.digraph import DirectedGraph

recipe = DirectedGraph()

# Adding the edges automatically adds the nodes.
recipe.add_edge('3/4 cup milk', '1 cup mix')
recipe.add_edge('1 egg', '1 cup mix')
recipe.add_edge('1 Tbl Oil', '1 cup mix')
recipe.add_edge('1 cup mix', 'pour 1/4 cup')
recipe.add_edge('1 cup mix', 'heat syrup')
recipe.add_edge('heat syrup', 'eat')
recipe.add_edge('heat griddle', 'pour 1/4 cup')
recipe.add_edge('pour 1/4 cup', 'turn when bubbly')
recipe.add_edge('turn when bubbly', 'eat')

# If this file is imported, do nothing.
# If it is run as a script, execute the app.
if __name__ == "__main__":
    print("To get a pancake, do these steps in this order:")
    print(recipe.topological_sort())
    print("Type a step without quotes to see which other ones depend on it.")
    print("To end the program, just type ENTER.")
    start = input("Recipe step: ")
    while start:
        if recipe.has_node(start):
            print("Steps that depend on", start, "are:")
            print("In breadth-first order:", recipe.visited_bfs(start)[1:])
            print("In depth-first order:", recipe.visited_dfs(start)[1:])
        else:
            print("The recipe hasn't that step.")
        start = input("Start step: ")

# Exercises
# ---------
#
# - What is `[1:]` doing and why?
# - A better indication of the number of sequential steps needed
#   is the length of the longest of all paths. Write a function to compute it.
