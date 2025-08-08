from app.main import add, subtract, multiply, divide

def test_add():
    assert add(3, 4) == 7

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(6, 7) == 42

def test_divide():
    assert divide(10, 2) == 5
