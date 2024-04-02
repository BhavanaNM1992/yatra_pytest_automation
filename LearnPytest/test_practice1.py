import pytest

@pytest.fixture(scope="session")
def setup():
    print("launch brwoser")
    print("login")
    print("open browser")
    yield
    print("logoff")
    print("close browser")




def test_login(setup):
    print("skdjds")

def test_loggoff(setup):
    print("heyyyyyyyy")

def test_add():
    assert 2+2==4


def pytest_addoption(parser):
    parser.addoption("--browser")

# def browser(request):
#     return request.