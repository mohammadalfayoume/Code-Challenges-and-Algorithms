# Write here the code challenge solution
# Write here the code challenge solution

class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.right=right
        self.left=left
class Tree:  
    def __init__(self):
        self.queue=[]
        self.root=None
    
    def sortedArrayToBST(self, nums):
        return self.makeBST(nums, 0, len(nums))
        
    def makeBST(self, nums, start, end):
        if start >= end: return None
        return Node(
            value=nums[ (start + end)//2 ],
            left=self.makeBST(nums, start, (start + end)//2),
            right=self.makeBST(nums, 1+((start+end)//2), end)
        )
    
    def BFS(self):
        '''
        this method to print the values of nodes by Breadth First Search
        input: None
        output: type:list
        '''
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
    
    # def insert(self,value):
    #     node= Node(value)
    #     if self.root==None:
    #         self.root=node
    #         return self.root
    #     else:
    #         current=self.root
    #         while True:
    #             if value==current.value:
    #                 return None
    #             if value<current.value:
    #                 if current.left==None:
    #                     current.left=node
    #                     return current.left
    #                 else:
    #                     current=current.left
    #             elif value>current.value:
    #                 if current.right==None:
    #                     current.right=node
    #                     return current.right
    #                 else:
    #                     current=current.right
    
    # def sortedArrayToBST(self,nums):
    #     def make_BST(nums,start,end):
    #         if start >= end:
    #             return None
    #         val=nums[ (start + end)//2 ]
    #         node=self.insert(val)
    #         node.left= make_BST(nums, start, (start + end)//2),
    #         node.right= make_BST(nums, 1+((start+end)//2), end)
            
        
    #     return make_BST(nums,0,len(nums))