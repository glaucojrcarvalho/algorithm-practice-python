class Stack:
    """
    Stack Data Structure
    - Follows the Last In, First Out (LIFO) principle.
    """

    def __init__(self):
        self.stack = []

    def push(self, value):
        """
        Push a value onto the stack.
        Time Complexity: O(1)
        """
        self.stack.append(value)

    def pop(self):
        """
        Remove and return the top value from the stack.
        Time Complexity: O(1)
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self):
        """
        Return the top value of the stack without removing it.
        Time Complexity: O(1)
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]

    def is_empty(self):
        """
        Check if the stack is empty.
        Time Complexity: O(1)
        """
        return len(self.stack) == 0

    def size(self):
        """
        Return the size of the stack.
        Time Complexity: O(1)
        """
        return len(self.stack)

    def __str__(self):
        """
        String representation of the stack.
        """
        return f"Stack({self.stack})"
