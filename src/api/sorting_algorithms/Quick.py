from api.sorting_algorithms.SortInterface import SortInterface
from random import randint

class Quick(SortInterface):
    
    def partition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1

    def quickSort(self, array, low, high):
        if low < high:
            pi = self.partition(array, low, high)
            self.quickSort(array, low, pi - 1)
            self.quickSort(array, pi + 1, high)

    def sort(self, arr):
        size = len(arr)
        try:
            self.quickSort(arr, 0, size - 1)
        except:
            print("Something went really wrong")
            print("This should be a Log error message")
        return arr

    def generateExampleArray(self, size):
        arr = []
        for _ in range(size):
            arr.append(randint(-1000, 1000))
        return arr