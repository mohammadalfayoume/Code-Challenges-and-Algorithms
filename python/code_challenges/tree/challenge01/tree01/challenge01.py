# Write here the code challenge solution

class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
class Tree:  
    def __init__(self):
        self.queue=[]
        self.root=None
    # def build(self,preorder,inorder):
    #     if inorder:
    #         root_val=preorder.pop(0)
    #         node= Node(root_val)

    #         idx= inorder.index(root_val)
    #         self.left_list=inorder[:idx]
    #         self.right_list=inorder[idx+1:]
            
    #         node.left=self.build(preorder,self.left_list)
    #         node.right=self.build(preorder,self.right_list)
            
    #         return node
    # def building_tree(self,preorder, inorder):
    #     node= Node(preorder[0])
    #     self.root=node
    #     def buildTree(preorder, inorder):
    #         if inorder:
    #             idx = inorder.index(preorder.pop(0))
    #             root = Node(inorder[idx])
    #             root.left = buildTree(preorder, inorder[:idx])
    #             root.right = buildTree(preorder, inorder[idx+1:])

    #             return root
    #     buildTree(preorder, inorder)
    
    def buildTree(self, preorder, inorder):
        '''
        method to build our binary tree by founding relation between preorder and inorder lists
        input: type:list , type:list
        return: type:object => root
        '''
        if inorder:
            INDEX = inorder.index(preorder.pop(0))
            root = Node(inorder[INDEX])
            root.left = self.buildTree(preorder, inorder[:INDEX])
            root.right = self.buildTree(preorder, inorder[INDEX+1:])
			
            return root
    
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
    
# tree=Tree()
# tree.root=tree.buildTree([5,1,8,4,10],[1,5,4,8,10])
# print(tree.BFS())