# Write your test here
from code_challenges.tree.challenge01.tree01.challenge01 import Tree

def test_one():
    tree=Tree()
    tree.root=tree.buildTree([3,9,20,15,7],[9,3,15,20,7])
    expected=[3,9,20,15,7]
    actual=tree.BFS()
    assert actual==expected
    
def test_two():
    tree=Tree()
    tree.root=tree.buildTree([-1],[-1])
    expected=[-1]
    actual=tree.BFS()
    assert actual==expected

def test_three():
    tree=Tree()
    tree.root=tree.buildTree([5,1,8,4,10],[1,5,4,8,10])
    expected=[5, 1, 8, 4, 10]
    actual=tree.BFS()
    assert actual==expected