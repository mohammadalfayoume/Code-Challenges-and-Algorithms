# Write here the code challenge solution
class Graph:
    def __init__(self):
        self.adjacencyList={}
    
    def addVertex(self,vertex):
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex]=[]
        # print(self.adjacencyList)
    
    def addEdge(self,v1,v2):
        self.adjacencyList[v1].append(v2)
        self.adjacencyList[v2].append(v1)
        # print(self.adjacencyList)
        
    def removeEdge(self,vertex1,vertex2):
        for v2 in self.adjacencyList[vertex1]:
            if v2==vertex2:
                self.adjacencyList[vertex1].remove(v2)
        for v1 in self.adjacencyList[vertex2]:
            if v1==vertex1:
                self.adjacencyList[vertex2].remove(v1)
        # print(self.adjacencyList)
    
    def removeVertex(self,vertex):
        while len(self.adjacencyList[vertex]):
            adjacentVertex= self.adjacencyList[vertex].pop()
            self.removeEdge(vertex,adjacentVertex)
        del self.adjacencyList[vertex]
        # print(self.adjacencyList)
        
    def depthFirstRecursive(self,start):
        result=[]
        visited={}
        
        def dfs(vertex):
            if not vertex:
                return None
            visited[vertex]=True
            result.append(vertex)
            for neighbor in self.adjacencyList[vertex]:
                if neighbor not in visited or not visited[neighbor]:
                    return dfs(neighbor)
        dfs(start)
        print(visited)
        return result

    def breadthFirst(self,start):
        queue=[start]
        result=[]
        visited={}
        visited[start]=True
        
        while len(queue):
            currentVertex=queue.pop(0)
            result.append(currentVertex)
            
            for neighbor in self.adjacencyList[currentVertex]:
                if neighbor not in visited or not visited[neighbor]:
                    visited[neighbor]=True
                    queue.append(neighbor)
        return result
            

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
g.addEdge("C","F")
g.addEdge("E","D")
g.addEdge("E","F")
g.addEdge("E","G")
g.addEdge("F","H")
g.addEdge("F","I")
g.addEdge("G","H")
g.addEdge("H","K")
g.addEdge("I","K")

print(g.breadthFirst("A"))