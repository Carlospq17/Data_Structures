from api.sorting_algorithms.SortInterface import SortInterface
from random import randint

class Heap(SortInterface):

    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
    
        if l < n and arr[i] < arr[l]:
            largest = l
    
        if r < n and arr[largest] < arr[r]:
            largest = r
    
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)
    
    
    def sort(self, arr):
        n = len(arr)
        try:
            for i in range(n//2, -1, -1):
                self.heapify(arr, n, i)

            for i in range(n-1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                self.heapify(arr, i, 0)
        except:
            print("Something went really wrong")
            print("This should be a Log error message")
        finally:
            return arr

    def generateExampleArray(self, size):
        arr = []
        for _ in range(size):
            arr.append(randint(-1000, 1000))
        return arr