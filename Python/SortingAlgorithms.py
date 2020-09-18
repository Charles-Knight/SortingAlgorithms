def BubbleSort(nums):
    def swap(l, idx1, idx2):
        l[idx1] = l[idx1] + l[idx2]
        l[idx2] = l[idx1] - l[idx2]
        l[idx1] = l[idx1] - l[idx2]
    
    swaps = -1
    while swaps != 0:
        swaps = 0
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                swap(nums, i, i+1)
                swaps += 1     

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
