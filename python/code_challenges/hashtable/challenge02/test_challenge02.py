# Write your test here
from .challenge02 import first_repeated

def test_01():
    s="ASAC is a department at LTUC. ASAC teaches programming in LTUC."
    expected= first_repeated(s)
    actual="ASAC"
    assert expected==actual
    
def test_02():
    s="I am learning programming at ASAC."
    expected= first_repeated(s)
    actual="No Repetition"
    assert expected==actual

def test_03():
    s="aa bb bb aa."
    expected= first_repeated(s)
    actual="aa"
    assert expected==actual