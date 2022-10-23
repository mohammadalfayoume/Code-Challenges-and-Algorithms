# Write your test here
import pytest
from challenge01 import Solution


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

    def delete_node(self,idx):
        '''
        input -> int

        return -> None
        '''
        node_to_be_deleted= self.get_node_from_index(idx)
        node_to_be_deleted.value=node_to_be_deleted.next.value
        node_to_be_deleted.next= node_to_be_deleted.next.next
        self.length -=1

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

########### Test 01 ###########
link1= LinkedList()
link1.append_by_tail(4)
link1.append_by_tail(5)
link1.append_by_tail(1)
link1.append_by_tail(9)

# print(link1.get_node_from_index(3))
print(link1.print_list_of_values())
# link1.delete_node(3)
# link1.insert_node(0,8)
# print(link1.print_list_of_values())

def test_delete_node_one(one):
    '''
        input -> object

        return -> boolean
        '''
    expected=[4,1,9]
    node_to_delete= link1.get_node(5)
    one.delete_node(node_to_delete)
    list_after_deleted_node= link1.print_list_of_values()
    actual= list_after_deleted_node
    assert actual==expected

########### Test 02 ###########
link2= LinkedList()
link2.append(4)
link2.append(5)
link2.append(1)
link2.append(9)

def test_delete_node_two(one):
    '''
        input -> object

        return -> boolean
        '''
    expected=[4,5,9]
    node_to_delete_02= link2.get_node(1)
    one.delete_node(node_to_delete_02)
    list_after_deleted_node= link2.print_list_of_values()
    actual= list_after_deleted_node
    assert actual==expected

########### Fixture Test ###########
@pytest.fixture
def one():
    '''
        input -> None

        return -> object
        '''
    delete_node_method= Solution()
    return delete_node_method