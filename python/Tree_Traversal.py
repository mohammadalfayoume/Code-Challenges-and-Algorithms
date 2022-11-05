# BFS
class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
        
        
class TreeTraversal:
    def __init__(self):
        self.queue=[]
        self.root=None
        
    
    def insert(self,value):
        node= Node(value)
        if self.root==None:
            self.root=node
        else:
            current=self.root
            while True:
                if value==current.value:
                    return None
                if value<current.value:
                    if current.left==None:
                        current.left=node
                        break
                    else:
                        current=current.left
                elif value>current.value:
                    if current.right==None:
                        current.right=node
                        break
                    else:
                        current=current.right
    
    def BFS(self):
        tree=[]
        if not self.root:
            return 'Empty tree'
        node= self.root
        self.queue.append(node)
        while self.queue:
            node= self.queue.pop(0)
            tree.append(node.value)
            if node.left != None:
                self.queue.append(node.left)
            if node.right != None:
                self.queue.append(node.right)
        return tree
    
    def DFS_preorder(self):
        tree=[]
        def traverse(node):
            tree.append(node.value)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return tree
    
    def DFS_postorder(self):
        tree=[]
        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            tree.append(node.value)
        traverse(self.root)
        return tree
    
    def DFS_inorder(self):
        tree=[]
        def traverse(node):
            if node.left:
                traverse(node.left)
            tree.append(node.value)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return tree
    
    def tree(self):
        self.root=self.DFS_preorder()[0]
        
            
    
tree=TreeTraversal()
tree.insert(10)
tree.insert(5)
tree.insert(13)
tree.insert(11)
tree.insert(2)
tree.insert(16)
tree.insert(7)

print(tree.BFS())
print(tree.DFS_preorder())
print(tree.DFS_postorder())
print(tree.DFS_inorder())