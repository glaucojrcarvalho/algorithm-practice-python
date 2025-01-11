import pytest
from data_structures.queue import Queue


def test_queue_operations():
    queue = Queue()

    # Test is_empty
    assert queue.is_empty() is True

    # Test enqueue
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    assert queue.is_empty() is False
    assert queue.size() == 3

    # Test peek
    assert queue.peek() == 10

    # Test dequeue
    assert queue.dequeue() == 10
    assert queue.dequeue() == 20
    assert queue.size() == 1

    # Test dequeue to empty the queue
    assert queue.dequeue() == 30
    assert queue.is_empty() is True

    # Test dequeue on empty queue raises error
    with pytest.raises(IndexError, match="dequeue from empty queue"):
        queue.dequeue()

    # Test peek on empty queue raises error
    with pytest.raises(IndexError, match="peek from empty queue"):
        queue.peek()

    print("All queue tests passed!")
