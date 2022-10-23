# Write here the code challenge solution
class Solution:
    def get_middle(self,head):
        # 1 => 2 => 3 => 4 => 5
        # 3 => 4 => 5
        nodes=[]
        current= head
        while current != None:
            nodes.append(current)
            current= current.next
        middle= len(nodes)//2
        middle_node=[]
        for i in range(middle,len(nodes)):
            middle_node.append(nodes[i].value)
        return middle_node