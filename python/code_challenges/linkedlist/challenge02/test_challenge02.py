# Write your test here
import pytest
from challenge02 import LinkedList

########### Test 01 ###########
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

########### Test 02 ###########

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

########### Fixture Test ###########

@pytest.fixture
def one():
    '''
        input -> None

        return -> object
        '''
    get_middle= LinkedList()
    return get_middle