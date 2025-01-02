from basic_algorithms.integer_searching import Searching

class Test:

    def test_searching(self):
        search = Searching()

        # Test Data
        sorted_array = [1, 3, 5, 7, 9, 11]
        unsorted_array = [4, 2, 7, 1, 9, 3]

        # Binary Search Tests (requires sorted array)
        assert search.binary(sorted_array, 7) == 3, "Binary search failed for target 7"
        assert search.binary(sorted_array, 1) == 0, "Binary search failed for target 1"
        assert search.binary(sorted_array, 11) == 5, "Binary search failed for target 11"
        assert search.binary(sorted_array, 10) == -1, "Binary search failed for non-existent target 10"

        # Linear Search Tests (works for unsorted arrays)
        assert search.linear(unsorted_array, 7) == 2, "Linear search failed for target 7"
        assert search.linear(unsorted_array, 1) == 3, "Linear search failed for target 1"
        assert search.linear(unsorted_array, 9) == 4, "Linear search failed for target 9"
        assert search.linear(unsorted_array, 10) == -1, "Linear search failed for non-existent target 10"

        print("All search tests passed!")

if __name__ == "__main__":
    test_instance = Test()

    test_instance.test_searching()