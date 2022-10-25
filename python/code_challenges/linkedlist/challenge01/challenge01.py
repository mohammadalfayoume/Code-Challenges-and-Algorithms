class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def append(self,value):
        '''
        input -> int or string

        return -> None
        '''
        new_node= Node(value)
        if self.head==None:
            self.head=new_node
        else:
            current=self.head
            while current.next != None:
                current=current.next
            current.next=new_node
        self.length +=1

    def get_node(self,value):
        '''
        input -> int or string

        return -> object
        '''
        current=self.head
        while current.value != value:
            current=current.next
        return current

    def print_list_of_values(self):
        '''
        input -> None

        return -> list
        '''
        values_in_list=[]
        if self.head==None:
            print("empty linked list")
        else:
            current=self.head
            while current != None:
                # print(current.value)
                values_in_list.append(current.value)
                current=current.next
            print(self.length)
        return values_in_list
    def __str__(self,node):
        '''
        input -> None

        return -> list
        '''
        if self.head==None:
            print("empty linked list")
        else:
            current=self.head
            while current != node:
                current=current.next
            print(self.length)
        return current
####################
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
    
    def insert_node(self,idx,value):
        '''
        input -> int, int or string

        return -> None
        '''
        new_node= Node(value)
        if idx==0:
            new_node.next=self.head
            self.head=new_node
        else:
            next_node= self.get_node_from_index(idx)
            new_node.next=next_node
            prev_node= self.get_node_from_index(idx-1)
            prev_node.next=new_node
        self.length +=1

    # def delete_node(self,idx):
    #     '''
    #     input -> int

    #     return -> None
    #     '''
    #     node_to_be_deleted= self.get_node_from_index(idx)
    #     node_to_be_deleted.value=node_to_be_deleted.next.value
    #     node_to_be_deleted.next= node_to_be_deleted.next.next
    #     self.length -=1

    def delete_node(self,node_to_be_deleted):
        '''
        input -> object

        return -> None
        '''
         # 1 -> 5 -> 7 -> 9 -> None
         # node_to_be_deleted=5
        node_to_be_deleted.value= node_to_be_deleted.next.value
        node_to_be_deleted.next= node_to_be_deleted.next.next
        # 1 -> 7 -> 9 -> None 

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
####################