import unittest
import src.model.graph as g


visited = []


def visit_node(current, goal):
    if current == goal:
        return True

    next_nodes = current.get_next()
    for next_node in next_nodes:
        if not visited.__contains__(next_node):
            visited.append(current)
            return visit_node(next_node, goal)


class MyTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.graph = g.Graph("simple_webservice", "simple")
        self.faulty_graph = g.Graph("faulty_graph", "simple")

    def test_start_to_end(self):
        global visited
        visited = []

        nodes = self.graph.get_nodes()
        start = nodes[0]
        goal = nodes[-1]

        self.assertTrue(visit_node(start, goal))

    def test_start_to_end_faulty(self):
        global visited
        visited = []

        nodes = self.faulty_graph.get_nodes()
        start = nodes[0]
        goal = nodes[-1]

        self.assertFalse(visit_node(start, goal))

    def test_all_initialized(self):
        nodes = self.graph.get_nodes()
        for node in nodes:
            self.assertIsNotNone(node.get_name())

            # first node and goal node have no previous node
            if node != nodes[0] and node != nodes[-1]:
                self.assertIsNotNone(node.get_prev())

            # goal node has no next node
            if node != nodes[-1]:
                self.assertIsNotNone(node.get_next())

            next_nodes = node.get_next()
            for next_node in next_nodes:
                self.assertIsNotNone(next_nodes[next_node])
