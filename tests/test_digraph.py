"""Unit tests for directed graphs."""

import unittest

from lib.digraph import DirectedGraph

class TestDigraph(unittest.TestCase):

    def setUp(self):
        # A brand new graph.
        self.new = DirectedGraph()
        # An empty graph. Tests removal of a single node.
        self.empty = DirectedGraph()
        self.empty.add_node(1)
        self.empty.remove_node(1)
        # A disconnected graph with two nodes.
        self.disconnected = DirectedGraph()
        self.disconnected.add_node(1)
        self.disconnected.add_node(2)
        # An connected graph with two nodes.
        self.connected = DirectedGraph()
        self.connected.add_edge(1, 2)

    def test_has_node(self):
        self.assertFalse(self.new.has_node(1))
        self.assertFalse(self.empty.has_node(1))
        self.assertFalse(self.disconnected.has_node('other'))
        self.assertTrue(self.disconnected.has_node(1))
        self.assertTrue(self.disconnected.has_node(2))
        self.assertTrue(self.connected.has_node(1))
        self.assertTrue(self.connected.has_node(2))

    def test_has_edge(self):
        self.assertFalse(self.new.has_edge(1, 2))
        self.assertFalse(self.empty.has_edge(1, 2))
        self.assertFalse(self.disconnected.has_edge(1, 2))
        self.assertTrue(self.connected.has_edge(1, 2))

    def test_weight(self):
        infinity = float('infinity')
        for graph in self.new, self.empty, self.disconnected, self.connected:
            self.assertEqual(graph.weight([1]), 0)        
            self.assertEqual(graph.weight([]), infinity)
            self.assertEqual(graph.weight([2, 2]), infinity)
            self.assertEqual(graph.weight([2, 1]), infinity)
        self.assertEqual(self.disconnected.weight([1, 2]), infinity)
        self.assertEqual(self.connected.weight([1, 2]), 1)

    def test_nodes(self):
        for graph in self.new, self.empty:
            self.assertEqual(graph.nodes(), set())
        for graph in self.disconnected, self.connected:
            self.assertEqual(graph.nodes(), {1, 2})
            
    def test_unweighted_edges(self):
        for graph in self.new, self.empty, self.disconnected:
            self.assertEqual(graph.unweighted_edges(), set())
        self.assertEqual(self.connected.unweighted_edges(), {(1, 2)}) 
            
    def test_weighted_edges(self):
        for graph in self.new, self.empty, self.disconnected:
            self.assertEqual(graph.weighted_edges(), set())
        self.assertEqual(self.connected.weighted_edges(), 
                         {(1, 2, 1)})

    def test_neighbours(self):
        self.assertEqual(self.disconnected.neighbours(1), set())
        self.assertEqual(self.disconnected.neighbours(2), set())
        self.assertEqual(self.connected.neighbours(1), {2})
        self.assertEqual(self.connected.neighbours(2), set())
        
    def test_visited_bfs(self):
        self.assertEqual(self.disconnected.visited_bfs(1), [1])       
        self.assertEqual(self.disconnected.visited_bfs(2), [2])
        self.assertEqual(self.connected.visited_bfs(1), [1, 2])
        self.assertEqual(self.connected.visited_bfs(2), [2])
        
    def test_unweighted_distance(self):
        infinity = float('infinity')
        self.assertEqual(self.disconnected.unweighted_distance(1, 2),
                         infinity)
        self.assertEqual(self.disconnected.unweighted_distance(2, 1),
                         infinity)
        self.assertEqual(self.disconnected.unweighted_distance(1, 1),
                         0)                         
        self.assertEqual(self.connected.unweighted_distance(1, 2), 1)
        self.assertEqual(self.connected.unweighted_distance(2, 1),
                         infinity)                         
        self.assertEqual(self.connected.unweighted_distance(1, 1), 0)
        
    def test_visited_dfs(self):
        self.assertEqual(self.disconnected.visited_dfs(1), [1])       
        self.assertEqual(self.disconnected.visited_dfs(2), [2])
        self.assertEqual(self.connected.visited_dfs(1), [1, 2])
        self.assertEqual(self.connected.visited_dfs(2), [2])
    
    def test_topological_sort(self):
        self.assertEqual(self.new.topological_sort(), [])
        self.assertEqual(self.empty.topological_sort(), [])
        self.assertIn(self.disconnected.topological_sort(), ([1, 2], [2, 1]))
        self.assertEqual(self.connected.topological_sort(), [1, 2])
        
    def test_shortest_path(self):
        self.assertEqual(self.disconnected.shortest_path(1, 2), [])
        self.assertEqual(self.disconnected.shortest_path(2, 1), [])
        self.assertEqual(self.connected.shortest_path(1, 2), [1, 2])
        self.assertEqual(self.connected.shortest_path(2, 1), [])
    
    def test_weighted_distance(self):
        infinity = float('infinity')
        self.assertEqual(self.disconnected.weighted_distance(1, 2), infinity)   
        self.assertEqual(self.disconnected.weighted_distance(2, 1), infinity)
        self.assertEqual(self.connected.weighted_distance(1, 2), 1)   
        self.assertEqual(self.connected.weighted_distance(2, 1), infinity)
        
    # The modifiers have already been partially tested through setUp()
    
    def test_add_node(self):
        self.disconnected.add_node(1)
        self.assertEqual(self.disconnected.nodes(), {1, 2})
    
    def test_add_edge(self):
        self.connected.add_edge(1, 2, 0.5)
        self.assertEqual(self.connected.weight([1, 2]), 0.5)
        
    def test_remove_edge(self):
        self.empty.remove_edge(1, 2)
        self.connected.remove_edge(1, 2)
        self.assertEqual(self.empty.weighted_edges(), set())
        self.assertEqual(self.connected.weighted_edges(), set())
        # removing an edge doesn't change the nodes
        self.assertEqual(self.connected.nodes(), self.disconnected.nodes())
        
    def test_remove_node(self):
        self.connected.remove_node(1)
        self.assertEqual(self.connected.nodes(), {2})
        self.assertEqual(self.connected.weighted_edges(), set())
        
        
        
        