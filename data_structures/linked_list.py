class Node:
    """
    Node for a Linked List.
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    Singly Linked List Data Structure
    - Each node points to the next node in the list.
    """

    def __init__(self):
        self.head = None

    def append(self, value):
        """
        Add a node to the end of the linked list.
        Time Complexity: O(n)
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, value):
        """
        Add a node to the beginning of the linked list.
        Time Complexity: O(1)
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        """
        Delete the first node with the given value.
        Time Complexity: O(n)
        """
        if self.head is None:
            raise ValueError("Value not found in the list")

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if current.next is None:
            raise ValueError("Value not found in the list")

        current.next = current.next.next

    def find(self, value):
        """
        Find a node with the given value.
        Time Complexity: O(n)
        Returns:
            Node: The node with the given value, or None if not found.
        """
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def is_empty(self):
        """
        Check if the linked list is empty.
        Time Complexity: O(1)
        """
        return self.head is None

    def to_list(self):
        """
        Convert the linked list to a Python list.
        Time Complexity: O(n)
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements

    def __str__(self):
        """
        String representation of the linked list.
        """
        values = self.to_list()
        return " -> ".join(map(str, values)) if values else "Empty Linked List"
