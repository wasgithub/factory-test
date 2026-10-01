from calc import add


def test_add_basic():
    assert add(1, 2) == 3


def test_add_zeros():
    assert add(0, 0) == 0


def test_add_negative():
    assert add(-1, 1) == 0


def test_add_floats():
    assert add(1.5, 2.5) == 4.0
