# Write your test here

from code_challenges.stack_queue.challenge02.stack02.challenge02 import Stack

s=Stack()

def test_one():
    expected=True
    actual=s.isValid('()')
    assert actual==expected

def test_two():
    expected=True
    actual=s.isValid('()[]{}')
    assert actual==expected

def test_three():
    expected=False
    actual=s.isValid('(]')
    assert actual==expected

def test_four():
    expected=True
    actual=s.isValid('{{[]}()}')
    assert actual==expected