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
# x= link1.get_node_from_index(0)
print(link1.get_middle())

def test_get_middle_node_one():
    '''
        input -> object

        return -> boolean
        '''
        #3 -> 4 -> 5
    expected=3
    middle_node_values=link1.get_middle()
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
print(link2.get_middle())



def test_get_middle_node_two():
    '''
        input -> object

        return -> boolean
        '''
    expected=4
    middle_node_values=link2.get_middle()
    actual= middle_node_values
    assert actual==expected
