class Sorting:
    """
    This class implements various sorting algorithms:
    - Bubble Sort
    - Selection Sort
    - Merge Sort
    - Quick Sort (In-Place and Non-In-Place)
    """

    def bubble(self, arr: list[int]) -> list[int]:
        """
        Bubble Sort: Repeatedly steps through the list, compares adjacent items, and swaps them if they are in the wrong order.
        - Time Complexity: O(n^2) in the worst and average cases; O(n) in the best case when the array is already sorted.
        - Space Complexity: O(1) (In-Place)
        """
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def selection(self, arr: list[int]) -> list[int]:
        """
        Selection Sort: Selects the smallest element from the unsorted part and swaps it with the first element of the unsorted part.
        - Time Complexity: O(n^2) in all cases.
        - Space Complexity: O(1) (In-Place)
        """
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def merge(self, arr: list[int]) -> list[int]:
        """
        Merge Sort: Divides the array into halves, sorts each half recursively, and then merges them.
        - Time Complexity: O(n log n) in all cases.
        - Space Complexity: O(n) (Not In-Place, requires extra space for merging)
        """
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            self.merge(left)
            self.merge(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        return arr

    def quick_non_inplace(self, arr: list[int]) -> list[int]:
        """
        Quick Sort (Non-In-Place): Uses a pivot element to partition the array into three lists: left, middle, and right.
        - Time Complexity: O(n log n) on average; O(n^2) in the worst case (poor pivot choice).
        - Space Complexity: O(n) (Not In-Place, requires extra space for partitions)
        """
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return self.quick_non_inplace(left) + middle + self.quick_non_inplace(right)

    def quick_inplace(self, arr: list[int], low: int, high: int) -> None:
        """
        Quick Sort (In-Place): Uses a pivot element to partition the array and sorts it within the same array.
        - Time Complexity: O(n log n) on average; O(n^2) in the worst case (poor pivot choice).
        - Space Complexity: O(log n) (In-Place, recursion stack space)
        """
        if low < high:
            pivot_index = self.partition(arr, low, high)
            self.quick_inplace(arr, low, pivot_index - 1)
            self.quick_inplace(arr, pivot_index + 1, high)

    def partition(self, arr: list[int], low: int, high: int) -> int:
        """
        Partition function for Quick Sort.
        - Moves elements smaller than the pivot to its left and larger elements to its right.
        """
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
