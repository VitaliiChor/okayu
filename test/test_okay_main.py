import random
import selenium
import pytest

@pytest.fixture()
def before_after():
    print('Before test')
    yield
    print('\nAfter test')


def test_can_check_num ():
    assert 1 != 2

def test_can_check_num2 (before_after):
    assert 1 == 1