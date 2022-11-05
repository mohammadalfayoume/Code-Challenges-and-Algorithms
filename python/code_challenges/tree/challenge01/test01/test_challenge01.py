# Write your test here
from code_challenges.tree.challenge01.tree01.challenge01 import Tree

def test_one():
    tree=Tree()
    tree.root=tree.buildTree([3,9,20,15,7],[9,3,15,20,7])
    expected=[3,9,20,15,7]
    actual=tree.BFS()
    assert actual==expected