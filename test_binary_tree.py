import pytest
from bst import BST, Node


@pytest.fixture
def bst():
    bst = BST()
    bst.insert(8)
    bst.insert(4)
    bst.insert(2)
    bst.insert(7)
    bst.insert(1)
    return bst

def test_insert():
    bst = BST()
    bst.insert(5)
    assert bst.root.value == 5

def test_search(bst):
    assert bst.search(7) == True
    assert bst.search(10) == False

def test_in_order_traversal(bst):
    assert bst.in_order_traversal(bst.root) == [1, 2, 4, 7, 8]

def test_find_min(bst):
    assert bst.find_min() == 1

def test_find_max(bst):
    assert bst.find_max() == 8

def test_height(bst):
    assert bst.height() == 4

def test_count_leaves(bst):
    assert bst.count_leaves() == 2

def test_serialize_and_deserialize(bst):
    serialized_tree = bst.serialize()
    new_bst = BST()
    new_bst.deserialize(serialized_tree)
    assert serialized_tree == new_bst.serialize()