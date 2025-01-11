class Queue:
    """
    Queue Data Structure
    - Follows the First In, First Out (FIFO) principle.
    """

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        """
        Add a value to the end of the queue.
        Time Complexity: O(1)
        """
        self.queue.append(value)

    def dequeue(self):
        """
        Remove and return the value from the front of the queue.
        Time Complexity: O(1) (for list with pop(0))
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.pop(0)

    def peek(self):
        """
        Return the value at the front of the queue without removing it.
        Time Complexity: O(1)
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.queue[0]

    def is_empty(self):
        """
        Check if the queue is empty.
        Time Complexity: O(1)
        """
        return len(self.queue) == 0

    def size(self):
        """
        Return the size of the queue.
        Time Complexity: O(1)
        """
        return len(self.queue)

    def __str__(self):
        """
        String representation of the queue.
        """
        return f"Queue({self.queue})"
