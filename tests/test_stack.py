import pytest
from ..stack.stack import Stack


@pytest.fixture
def stack():
    return Stack()


def test_constructor():
    s = Stack()
    assert isinstance(s, Stack)
    assert len(s) == 0


def test_push(stack):
    stack.push(3)
    assert len(stack) == 1
    stack.push('hi there')
    assert len(stack) == 2


def test_pop(stack):
    stack.push('yeah')
    assert stack.pop() == 'yeah'
    assert len(stack) == 0
    assert stack.pop() is None
