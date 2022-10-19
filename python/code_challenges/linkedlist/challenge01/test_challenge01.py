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
        self.length=0
    def append(self,value):
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
        current=self.head
        while current.value != value:
            current=current.next
        return current

    def print_list_of_values(self):
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

########### Test 01 ###########
link1= LinkedList()
link1.append(4)
link1.append(5)
link1.append(1)
link1.append(9)

def test_delete_node_one(one):
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
    expected=[4,5,9]
    node_to_delete_02= link2.get_node(1)
    one.delete_node(node_to_delete_02)
    list_after_deleted_node= link2.print_list_of_values()
    actual= list_after_deleted_node
    assert actual==expected

########### Fixture Test ###########
@pytest.fixture
def one():
    delete_node_method= Solution()
    return delete_node_method