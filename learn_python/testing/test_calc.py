import pytest

from learn_python.pythoncode.calculator import Calculator


class TestCalc:

    def test_add(self):
        calc = Calculator()
        result =calc.add(1,1)
        assert 2 == result
if __name__ == '__main__':
    pytest.main()