import pytest
from bst import BST


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

def test_serialize(bst):
    serialized_tree = bst.serialize()
    assert isinstance(serialized_tree, str)

def test_deserialize(bst):
    serialized_tree = bst.serialize()
    new_bst = BST()
    new_bst.deserialize(serialized_tree)
    assert new_bst.in_order_traversal(new_bst.root) == bst.in_order_traversal(bst.root)
    assert new_bst.serialize() == serialized_tree