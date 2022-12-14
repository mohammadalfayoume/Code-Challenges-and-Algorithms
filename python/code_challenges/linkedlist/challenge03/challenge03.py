# Write here the code challenge solution

class Node:
    '''
    Class to create a nodes
    '''
    def __init__(self,value):
        self.value=value
        self.next=None
    
class LinkedList:
    '''
    Class to create a Linked list
    '''
    def __init__(self):
        '''
        Constructor
        input: None
        output: None
        '''
        self.head=None
        self.tail=None
        self.length=0

    def print_list_of_values(self):

        '''
        This method print a list of values for each node

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

    def append_by_tail(self,value):
        '''
        Method use to add new node to the linked list

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

    def removeNthFromEnd(self, n):
        """
        Method to remove specific node based on the number of node from end of linked list
        :type n: int
        :rtype: ListNode
        """
        nodes=[]
        current= self.head
        while current != None:
            nodes.append(current)
            current=current.next   
        if len(nodes)==1:
            self.head=None
            return self.head
        idx=len(nodes)-n
        idx2=len(nodes)-(n+1)
        node_to_be_deleted= nodes[idx]
        prev_node= nodes[idx2]
        if node_to_be_deleted.next==None:
            node_to_be_deleted=None
            prev_node.next=None
            return self.head
        node_to_be_deleted.value=node_to_be_deleted.next.value
        node_to_be_deleted.next=node_to_be_deleted.next.next
        return self.head
