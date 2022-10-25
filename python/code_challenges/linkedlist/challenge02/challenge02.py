# Write here the code challenge solution
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def get_node_from_index(self,idx):
        '''
        input -> int

        return -> object
        '''
        if self.head==None:
            print("Empty LL")
        else:
            current= self.head
            counter=0
            while counter != idx:
                current = current.next
                counter +=1
            return current
    

    def append_by_tail(self,value):
        '''
        input -> int or string

        return -> None
        '''
        new_node= Node(value)
        if self.head == None:
            self.head=new_node
            self.tail=self.head
        else:
            current=self.tail
            current.next=new_node
            self.tail=new_node
    
    def get_middle(self,head):
        '''
        input -> object

        return -> list
        '''
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