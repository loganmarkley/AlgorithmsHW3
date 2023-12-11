# Author : Logan Markley
# Due Date : 12 / 11 / 2023
# Course : CS 2500 (Algorithms)
# Semester : Fall 2023
# Professor : Dr. Morales

# bubble sorts arr and returns the number of array swap operations performed
def bubbleSort(inputArr: list[int], size: int) -> None:
    numArraySwaps = 0
    for i in range(size):
        for j in range(size - 1 - i):
            if inputArr[j+1] < inputArr[j]:
                inputArr[j], inputArr[j+1] = inputArr[j+1], inputArr[j]
                numArraySwaps += 1
    
    return numArraySwaps

# partitions the subarray and returns how many array swap operations are performed
def hoarePartition(arr: list[int], left: int, right: int, swap_count: int) -> (int, int):
    pivot = arr[left]
    i = left
    j = right
    
    while i < j:
        while i < j and arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        swap_count += 1
    
    arr[i], arr[j] = arr[j], arr[i]
    swap_count += 1
    arr[left], arr[j] = arr[j], arr[i]
    swap_count += 1
    
    return j, swap_count

# quick sorts arr and returns the number of array swap operations performed
def quickSort(arr: list[int], left: int, right: int, swap_count: int) -> int:
    if left < right:
        p, swap_count = hoarePartition(arr, left, right, swap_count)
        swap_count = quickSort(arr, left, p-1, swap_count)
        swap_count = quickSort(arr, p+1, right, swap_count)
    
    return swap_count

if __name__ == "__main__":
    arraySize = int(input())
    arr = []
    for i in range(arraySize):
        arr.append(int(input()))
    
    bubbleCopy = arr.copy()
    quickCopy = arr.copy()
    
    print(bubbleSort(bubbleCopy, arraySize))
    print(quickSort(quickCopy, 0, arraySize-1, 0))
    
    
