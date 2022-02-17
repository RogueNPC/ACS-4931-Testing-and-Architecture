from cmath import exp
import unittest
import pytest
import math
from carbon_dating import get_age_carbon_14_dating

# Write a unit test which feed 0.35 to the function.
# The result should be '8680.34'. Does the function handles
# every possible input correctly? What if the input is zero
# or negative?
# Add the necessary logic to make sure the function handle
# every possible input properly. Then write a unit test againt
# this special case.

def test_get_age_carbon_14_dating_normal_use_case():
    expected_output = math.log(0.35) / -0.693 * 5730
    assert math.isclose(get_age_carbon_14_dating(0.35), expected_output)

def test_get_age_carbon_14_dating_zero_edge_case():
    assert get_age_carbon_14_dating(0) == "Error, your carbon_14_ratio must be greater than 0."

def test_get_age_carbon_14_dating_negative_edge_case():
    assert get_age_carbon_14_dating(-0.35) == "Error, your carbon_14_ratio must be greater than 0."