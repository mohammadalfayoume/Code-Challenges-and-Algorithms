# Write your test here
from code_challenges.tree.challenge03.tree03.challenge03 import Tree

tree=Tree()

def test_one():
    tree.root=tree.sortedArrayToBST([-10,-3,0,5,9])
    expected=[0,-3,9,-10,5]
    actual=tree.BFS()
    assert actual==expected

def test_two():
    tree.root=tree.sortedArrayToBST([1,3])
    expected=[3,1]
    actual=tree.BFS()
    assert actual==expected

def test_three():
    tree.root=tree.sortedArrayToBST([0,1,2,3,4,5])
    expected=[3, 1, 5, 0, 2, 4]
    actual=tree.BFS()
    assert actual==expected
