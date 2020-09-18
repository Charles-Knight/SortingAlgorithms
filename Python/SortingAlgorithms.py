def BubbleSort(nums):
    pass

def SelectionSort(nums):
    for position in range(0, len(nums)):
        index_of_minimum = position
        for index in range(position, len(nums)):
            if nums[index] < nums[index_of_minimum]:
                index_of_minimum = index
        nums.insert(position, nums[index_of_minimum])
        del nums[index_of_minimum + 1]

def InsertionSort(nums):
    pass

def MergeSort(nums):
    pass

def ShellSort(nums):
    pass

def QuickSort(nums):
    pass

def CountingSort(nums):
    pass

def RadixSort(nums):
    pass

nums = [10, 9, 8]
SelectionSort(nums)
print(nums)


