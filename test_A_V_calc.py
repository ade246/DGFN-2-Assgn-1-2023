'''
# test_A_V_calc.py

TPRG 2131 Fall 2023 Assignment 1
October,11 2023
KHARI WALLACE, 100807131,
Khari Wallace <khari.wallace@dcmail.ca>
'''

from assertions import add2
import A_V_calc
import pytest



def test_calculate_volume_1():
    # Test calculation 1 (Sphere volume)
    result = A_V_calc.calculate_volume_1([3.0])  # Replace with the appropriate radius
    assert result == 200  # expected result
    assert result == 113.09733552923254  # Replace with expected result
    assert result == 116.29333552923254  # Replace with the expected result
