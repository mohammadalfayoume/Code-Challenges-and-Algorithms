class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
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
                        
    def search(self,value):
        if self.root==None:
            return False
        elif self.root.value==value:
            return True
        else:
            current=self.root
            while True:
                if value<current.value:
                    if current.left==None:
                        return False
                    elif current.left.value==value:
                        return True
                    else:
                        current=current.left
                elif value>current.value:
                    if current.right==None:
                        return False
                    elif current.right.value==value:
                        return True
                    else:
                        current=current.right

    def find(self,value):
        if self.root==None:
            return False
        current= self.root
        while current:
            if value < current.value:
                current=current.left
            elif value> current.value:
                current=current.right
            else:
                return True
        return False
            
tree=BinarySearchTree()
tree.insert(10)
tree.insert(5)
tree.insert(13)
tree.insert(11)
tree.insert(2)
tree.insert(16)
tree.insert(7)

# print(tree.search(25))
# print(tree.find(100))
