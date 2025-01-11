import pytest
from data_structures.linked_list import LinkedList


def test_linked_list_operations():
    linked_list = LinkedList()

    # Test is_empty
    assert linked_list.is_empty() is True

    # Test append
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    assert linked_list.to_list() == [10, 20, 30]

    # Test prepend
    linked_list.prepend(5)
    assert linked_list.to_list() == [5, 10, 20, 30]

    # Test find
    node = linked_list.find(20)
    assert node is not None and node.value == 20

    # Test delete
    linked_list.delete(20)
    assert linked_list.to_list() == [5, 10, 30]

    # Test delete head
    linked_list.delete(5)
    assert linked_list.to_list() == [10, 30]

    # Test delete non-existent value
    with pytest.raises(ValueError, match="Value not found in the list"):
        linked_list.delete(100)

    # Test is_empty after deleting all elements
    linked_list.delete(10)
    linked_list.delete(30)
    assert linked_list.is_empty() is True

    print("All linked list tests passed!")
