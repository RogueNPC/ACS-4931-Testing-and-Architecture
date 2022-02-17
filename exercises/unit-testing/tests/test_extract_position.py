import pytest
from extract_position import extract_position

def test_extract_position_normal_use_case_error():
    result1 = '|error| numerical calculations could not converge.'
    assert extract_position(result1) == None

def test_extract_position_normal_use_case():
    result2 = '|update| the positron location in the particle accelerator is x:21.432'
    assert extract_position(result2) == '21.432'

def test_extract_position_edge_case():
    result3 = 'x:'
    assert extract_position(result3) == ''