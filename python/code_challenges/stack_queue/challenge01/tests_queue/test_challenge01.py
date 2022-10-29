# Write your test here
import pytest
from code_challenges.stack_queue.challenge01.stack.challenge01 import Queue

q=Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)

def test_push():
    expected=[1,2,3,4]
    actual= q.s1
    assert actual==expected

def test_peek():
    expected=1
    peek_val=q.peek()
    actual= peek_val
    assert actual==expected

def test_pop():
    expected=1
    pop_val=q.pop()
    actual= pop_val
    assert actual==expected
    assert q.s1==[2,3,4]

def test_empty():
    assert q.empty()==False

    
# stack1=Stack()

# stack1.push(1)
# stack1.push(2)
# stack1.push(3)
# stack1.push(4)
# stack1.push(5)


# stack2= Stack()
# stack2.push(stack1.pop())
# stack2.push(stack1.pop())
# stack2.push(stack1.pop())
# stack2.push(stack1.pop())
# stack2.push(stack1.pop())


# def test_one():
#     expected=1
#     peek=stack2.peek()
#     actual=peek
#     assert actual==expected

# def test_stack1():
#     expected=[1,2,3,4,5]
#     actual=stack1.list
#     assert actual==expected

# def test_stack2():
#     expected=[5,4,3,2,1]
#     actual=stack2.list
#     assert actual==expected

# def test_two():
#     expected=1
#     pop=stack2.pop()
#     actual=pop
#     assert actual==expected

# def test_three():
#     expected=False
#     is_empty= stack2.empty()
#     actual=is_empty
#     assert actual==expected

