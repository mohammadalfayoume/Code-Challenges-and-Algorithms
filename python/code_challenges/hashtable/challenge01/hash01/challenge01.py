# Write here the code challenge solution

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
        self.queue=[]
    
    def insert(self,val):
        node= Node(val)
        if not self.root:
            self.root=node
        def helper(root):
                
            if val<root.val and root.left:
                helper(root.left)
            if val<root.val and not root.left:
                root.left=node
                return
            if val>root.val and root.right:
                helper(root.right)
            if val>root.val and not root.right:
                root.right=node
                return
        helper(self.root)
        
    
    def BFS(self):
        tree=[]
        if not self.root:
            return 'Empty tree'
        node= self.root
        self.queue.append(node)
        while self.queue:
            node= self.queue.pop(0)
            tree.append(node.val)
            if node.left != None:
                self.queue.append(node.left)
            if node.right != None:
                self.queue.append(node.right)
        return tree
    
    def sum_two(self,k):
        dic={}
        def dfs(root,k):
            if root.val not in dic:
                dic[root.val]=root.val   
            if k-root.val in dic and k-root.val != root.val:
                return True
            if root.left and root.right:
                return dfs(root.left,k) or dfs(root.right,k)
            elif root.left:
                return dfs(root.left,k)
            elif root.right:
                return dfs(root.right,k)
            else:
                return False
        return dfs(self.root,k)

# tree= BST()
# root=tree.root
# tree.insert(10)
# tree.insert(8)
# tree.insert(6)
# tree.insert(15)

# print(tree.sum_two(14))

# print(tree.BFS())


class HashTable:
    def __init__(self,size=4):
        self.size=size
        self.map=[None]*size
        
    def _hash(self,key):
        sum_of_ascii=0
        for char in key:
            ascii_of_char= ord(char)
            sum_of_ascii +=ascii_of_char
        prime_num=11
        index= (sum_of_ascii*prime_num) % self.size
        return index
    
    def set(self,key,val):
        index= self._hash(key)
        if not self.map[index]:
            self.map[index]=[]
        self.map[index].append([key,val])
        # print(self.map)

    def get(self,key):
        index= self._hash(key)
        if self.map[index]:
            for i,lst in enumerate(self.map[index]):
                if lst[0]==key:
                    # print(lst[1])
                    return lst[1]
        return None
            
# create instanse
# ht= HashTable()
# set
# ht.set('mohammad','alfayoume')
# ht.set('lujain','aljarrah')
# ht.set('islam','alghol')
# ht.set('abed','alasal')
# get
# ht.get('abed')

