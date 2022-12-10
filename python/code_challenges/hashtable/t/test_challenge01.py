from code_challenges.hashtable.h.challenge01 import BST
tree= BST()
tree.insert(5)
tree.insert(3)
tree.insert(6)
tree.insert(2)
tree.insert(4)
tree.insert(7)
def one():
    expected=True
    actual= tree.sum_two(8)
    assert actual==expected
def two():
    expected=False
    actual= tree.sum_two(30)
    assert actual==expected
def three():
    expected=True
    actual= tree.sum_two(12)
    assert actual==expected