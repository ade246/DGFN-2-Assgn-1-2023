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



def test_calculate_volume_2():
    # Test calculation 2 (Cube volume)
    result = A_V_calc.calculate_volume_2([2.0])  # Replace with the appropriate side length
    assert result == 10.0  # expected result
    assert result == 8.0  # Replace with the expected result
    assert result == 14.0  # Replace with the expected result



def test_calculate_area_1():
    # Test calculation 3 (Rectangle area)
    result = A_V_calc.calculate_area_1([4.0, 5.0])  # Replace with the appropriate length and width
    assert result == 10.0  # expected result
    assert result == 20.0  # Replace with the expected result
    assert result == 40.0  # Replace with the expected result



def test_calculate_area_2():
    # Test calculation 4 (Triangle area)
    result = A_V_calc.calculate_area_2([6.0, 8.0])  # Replace with the appropriate base and height
    assert result == 10.0  # Replace with the expected result
    assert result == 24.0  # expected result
    assert result == 14.0  # Replace with the expected result