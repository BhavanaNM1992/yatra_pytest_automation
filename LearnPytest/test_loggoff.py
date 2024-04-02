import pytest

def test_login():
    print("skdjds")

def test_loggoff():
    print("heyyyyyyyy")

@pytest.mark.xfail
def test_add():
    assert 2+2==4