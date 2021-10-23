import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 4, 3) == 12

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 9, 3) == 3

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 7, 2) == 5

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 3, 5) == 8
