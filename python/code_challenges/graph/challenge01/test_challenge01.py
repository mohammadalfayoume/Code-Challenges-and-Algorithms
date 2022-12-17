# Write your test here
from .challenge01 import Graph

g=Graph()

g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")
g.addVertex("G")
g.addVertex("H")
g.addVertex("I")
g.addVertex("K")


g.addEdge("A", "B")
g.addEdge("A", "C")
g.addEdge("A","E")
g.addEdge("B","D")
g.addEdge("D","E")
g.addEdge("C","F")
g.addEdge("E","F")
g.addEdge("E","G")
g.addEdge("H","G")
g.addEdge("H","F")
g.addEdge("I","F")
g.addEdge("I","K")
g.addEdge("K","H")

def test_01():
    expected=['A', 'B', 'C', 'E', 'D', 'F', 'G', 'H', 'I', 'K']
    actual =g.breadthFirst("A")
    assert expected==actual