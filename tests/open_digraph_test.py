import sys
import os
root = os.path.normpath(os.path.join(__file__, './../..'))
sys.path.append(root)# allows us to fetch files from the project root
import unittest
from modules.open_digraph import *


class InitTest(unittest.TestCase):

    def test_init_node(self):
        n0 = node(0, 'i', {}, {1:1})
        self.assertEqual(n0.id, 0)
        self.assertEqual(n0.label, 'i')
        self.assertEqual(n0.parents, {})
        self.assertEqual(n0.children, {1:1})
        self.assertIsInstance(n0, node)


class NodeTest(unittest.TestCase):
    def setUp(self):
        self.n0 = node(0, 'a', [], [1])
    def test_get_id(self):
        self.assertEqual(self.n0.get_id(), 0)
    def test_get_label(self):
        self.assertEqual(self.n0.get_label(), 'a')
    def test_copy(self) :
        self.assertIsNot(self.n0.copy(), self.n0)

class OpenDigraphTest(unittest.TestCase) :
    def setUp(self) :
        n0 = node(0, 'i', {}, {1:1})
        self.b0 = open_digraph([1,0],[],[n0,n0])
    def test_get_input_ids(self):
        self.assertEqual(self.b0.get_input_ids(), [1,0])
    def test_copy(self) :
        self.assertIsNot(self.b0.copy(), self.b0)


if __name__ == '__main__': # the following code is called only when
     unittest.main() # precisely this file is run 




