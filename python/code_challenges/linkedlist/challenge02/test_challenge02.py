# Write your test here
import pytest
from challenge02 import Solution
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
    
    # def get_middle(self,head):
    #     # 1 => 2 => 3 => 4 => 5
    #     # 3 => 4 => 5
    #     nodes=[]
    #     current= head
    #     # print(current)
    #     while current != None:
    #         nodes.append(current)
    #         current= current.next
    #     middle= len(nodes)//2
    #     middle_node=[]
    #     for i in range(middle,len(nodes)):
    #         middle_node.append(nodes[i].value)
    #     return middle_node

link1= LinkedList()
link1.append_by_tail(1)
link1.append_by_tail(2)
link1.append_by_tail(3)
link1.append_by_tail(4)
link1.append_by_tail(5)


def test_get_middle_node_one(one):
    '''
        input -> object

        return -> boolean
        '''
    expected=[3,4,5]
    head= link1.get_node_from_index(0)
    middle_node_values=one.get_middle(head)
    actual= middle_node_values
    assert actual==expected


link2= LinkedList()
link2.append_by_tail(1)
link2.append_by_tail(2)
link2.append_by_tail(3)
link2.append_by_tail(4)
link2.append_by_tail(5)
link2.append_by_tail(6)


def test_get_middle_node_two(one):
    '''
        input -> object

        return -> boolean
        '''
    expected=[4,5,6]
    head= link2.get_node_from_index(0)
    middle_node_values=one.get_middle(head)
    actual= middle_node_values
    assert actual==expected

@pytest.fixture
def one():
    '''
        input -> None

        return -> object
        '''
    get_middle= Solution()
    return get_middle