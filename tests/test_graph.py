"""Unit tests for undirected graphs."""

import unittest

from lib.graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        # A brand new graph.
        self.new = Graph()
        # A disconnected graph
        self.disconnected = Graph()
        self.disconnected.add_edge(1, 2)
        self.disconnected.add_edge(3, 4)
        # A complete graph
        self.complete = Graph()
        self.complete.add_edge(1, 2, 3)
        self.complete.add_edge(2, 3, 5)
        self.complete.add_edge(3, 4, 7)
        self.complete.add_edge(4, 1, 5)
        self.complete.add_edge(1, 3, 4)
        self.complete.add_edge(2, 4, 6)

    def test_has_edge(self):
        self.assertFalse(self.new.has_edge(1, 2))
        self.assertFalse(self.disconnected.has_edge(2, 3))
        self.assertFalse(self.disconnected.has_edge(1, 1))
        self.assertFalse(self.disconnected.has_edge(5, 1))
        self.assertTrue(self.disconnected.has_edge(2, 1))

    def test_unweighted_edges(self):
        self.assertEqual(self.new.unweighted_edges(), set())
        self.assertEqual(len(self.disconnected.unweighted_edges()), 2)
        self.assertEqual(len(self.complete.unweighted_edges()), 6)
        for graph in self.disconnected, self.complete:
            edges = graph.unweighted_edges()
            for (source, target) in edges:
                self.assertNotIn((target, source), edges)

    def test_weighted_edges(self):
        self.assertEqual(self.new.weighted_edges(), set())
        self.assertEqual(len(self.disconnected.weighted_edges()), 2)
        self.assertEqual(len(self.complete.weighted_edges()), 6)
        edges = self.disconnected.weighted_edges()
        for (source, target, weight) in edges:
            self.assertEqual(weight, 1)
            self.assertNotIn((target, source, weight), edges)
        edges = self.complete.weighted_edges()
        for (source, target, weight) in edges:
            self.assertEqual(weight, source + target)
            self.assertNotIn((target, source, weight), edges)

    def test_topological_sort(self):
        for graph in self.new, self.disconnected, self.complete:
            self.assertEqual(graph.topological_sort(), [])

    def test_best_tour(self):
        self.assertIn(
            self.complete.best_tour(),
            [[1, 2, 3, 4, 1], [2, 3, 4, 1, 2], [3, 4, 1, 2, 3], [4, 1, 2, 3, 4]],
        )

    def test_minimum_spanning_tree(self):
        mst = self.complete.minimum_spanning_tree(4)
        self.assertEqual(mst.nodes(), self.complete.nodes())
        self.assertEqual(mst.unweighted_edges(), {(4, 1), (1, 2), (1, 3)})
