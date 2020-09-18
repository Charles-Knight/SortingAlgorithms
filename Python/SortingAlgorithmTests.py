import unittest
import SortingAlgorithms

class TestSortingAlgorithms(unittest.TestCase):
    
    def test_selection(self):
        nums = [10, 5, 15, -1, 0]
        self.assertEqual(sorted(nums), SortingAlgorithms.SelectionSort(nums))


if __name__ == "__main__":
    unittest.main()
