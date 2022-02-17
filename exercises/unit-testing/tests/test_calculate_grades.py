import unittest
from unittest import mock
import pytest
import math
from calculate_grades import *

def test_caluclate_stat_normal_case():
    grade_list = [99,88,77,66,55]

    total = 0
    for grade in grade_list:
        total = total + grade
    mean = total / len(grade_list)
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list))

    assert calculate_stat(grade_list) == (mean, sd)