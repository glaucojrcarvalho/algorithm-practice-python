class Searching:

    def binary(self, arr: list[int], target: int) -> int:
        """
        Binary Search Algorithm
        - Time Complexity: O(log n)
        - Space Complexity: O(1)
        - Requires a sorted array.

        Parameters:
        - arr: List of sorted integers.
        - target: The element to find.

        Returns:
        - Index of the target element, or -1 if not found.
        """
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    def linear(self, arr: list[int], target: int) -> int:
        """
        Linear Search Algorithm
        - Time Complexity: O(n)
        - Space Complexity: O(1)

        Parameters:
        - arr: List of integers.
        - target: The element to find.

        Returns:
        - Index of the target element, or -1 if not found.
        """
        for i in range(len(arr)):
            if arr[i] == target:
                return i

        return -1