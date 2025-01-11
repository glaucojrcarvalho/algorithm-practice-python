import pytest
from data_structures.stack import Stack


def test_stack_operations():
    stack = Stack()

    # Test is_empty
    assert stack.is_empty() is True

    # Test push
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert stack.is_empty() is False
    assert stack.size() == 3

    # Test peek
    assert stack.peek() == 30

    # Test pop
    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.size() == 1

    # Test pop to empty the stack
    assert stack.pop() == 10
    assert stack.is_empty() is True

    # Test pop on empty stack raises error
    with pytest.raises(IndexError, match="pop from empty stack"):
        stack.pop()

    # Test peek on empty stack raises error
    with pytest.raises(IndexError, match="peek from empty stack"):
        stack.peek()

    print("All stack tests passed!")
