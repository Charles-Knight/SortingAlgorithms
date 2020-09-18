import unittest
import SortingAlgorithms

class TestSortingAlgorithms(unittest.TestCase):
    
    def test_bubble(self):
        nums = [10, 5, 15, -1, 0]
        sorted_nums = list(nums)
        SortingAlgorithms.BubbleSort(sorted_nums)
        self.assertEqual(sorted(nums), sorted_nums)

    def test_selection(self):
        nums = [10, 5, 15, -1, 0]
        sorted_nums = list(nums)
        SortingAlgorithms.SelectionSort(sorted_nums)
        self.assertEqual(sorted(nums), sorted_nums)

    def test_insertion(self):
        nums = [10, 5, 15, -1, 0]
        sorted_nums = list(nums)
        SortingAlgorithms.InsertionSort(sorted_nums)
        self.assertEqual(sorted(nums), sorted_nums)

    def test_merge(self):
        nums = [10, 5, 15, -1, 0]
        sorted_nums = list(nums)
        SortingAlgorithms.MergeSort(sorted_nums)
        self.assertEqual(sorted(nums), sorted_nums)

    def test_shell(self):
        nums = [10, 5, 15, -1, 0]
        sorted_nums = list(nums)
        SortingAlgorithms.ShellSort(sorted_nums)
        self.assertEqual(sorted(nums), sorted_nums)
    
    def test_quick(self):
        nums = [10, 5, 15, -1, 0]
        sorted_nums = list(nums)
        SortingAlgorithms.QuickSort(sorted_nums)
        self.assertEqual(sorted(nums), sorted_nums)
    
    def test_counting(self):
        nums = [10, 5, 15, -1, 0]
        sorted_nums = list(nums)
        SortingAlgorithms.CountingSort(sorted_nums)
        self.assertEqual(sorted(nums), sorted_nums)
    
    def test_radix(self):
        nums = [10, 5, 15, -1, 0]
        sorted_nums = list(nums)
        SortingAlgorithms.RadixSort(sorted_nums)
        self.assertEqual(sorted(nums), sorted_nums)
    

if __name__ == "__main__":
    unittest.main()
