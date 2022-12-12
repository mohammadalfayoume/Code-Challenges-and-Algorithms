from code_challenges.hashtable.challenge01.hash01.challenge01 import BST
tree= BST()
tree.insert(5)
tree.insert(3)
tree.insert(6)
tree.insert(2)
tree.insert(4)
tree.insert(7)

# print(tree.sum_two(21))

print(tree.BFS())
def test_one():
    expected=True
    actual= tree.sum_two(8)
    assert actual==expected
def test_two():
    expected=False
    actual= tree.sum_two(30)
    assert actual==expected
def test_three():
    expected=True
    actual= tree.sum_two(12)
    assert actual==expected