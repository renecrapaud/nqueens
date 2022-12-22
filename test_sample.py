import app

def test_8Qs():
    assert app.ini(8) == 'Total: 92'
def test_9Qs():
    assert app.ini(9) == 'Total: 352'
def test_10Qs():
    assert app.ini(10) == 'Total: 724'
def test_11Qs():
    assert app.ini(11) == 'Total: 2680'