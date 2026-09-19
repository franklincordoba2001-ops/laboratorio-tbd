from main import Calculator


def test_suma():
    calc = Calculator()
    assert calc.suma(2, 3) == 5