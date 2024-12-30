from ..integer_sorting import Sorting

class Test:

    def test_sorting(self):
        sorter = Sorting()

        test_cases = [
            ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Already sorted
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Reversed order
            ([], []),  # Empty list
            ([7], [7]),  # Single element
            ([3, 1, 2, 3], [1, 2, 3, 3]),  # With duplicates
        ]

        for method in ['bubble', 'selection', 'merge', 'quick_non_inplace']:
            print(f"\nTesting {method} sort:")
            print("...")
            for input_array, expected in test_cases:
                sorted_array = getattr(sorter, method)(input_array.copy())
                assert sorted_array == expected, f"{method} failed for {input_array}"

        print("\nTesting quick sort (in-place):")
        print("...")
        for input_array, expected in test_cases:
            array = input_array.copy()
            sorter.quick_inplace(array, 0, len(array) - 1)
            assert array == expected, f"Quick sort failed for {input_array}"

        print("All tests passed!")


if __name__ == "__main__":
    test_instance = Test()

    test_instance.test_sorting()
