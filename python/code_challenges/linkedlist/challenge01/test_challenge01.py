# Write your test here
import pytest
from challenge01 import LinkedList

########### Test 01 ###########
link1= LinkedList()
link1.append_by_tail(4)
link1.append_by_tail(5)
link1.append_by_tail(1)
link1.append_by_tail(9)

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
    delete_node_method= LinkedList()
    return delete_node_method