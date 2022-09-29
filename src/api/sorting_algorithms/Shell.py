from api.sorting_algorithms.SortInterface import SortInterface
from random import randint

class Shell(SortInterface):
    
    def shellSort(self, array, n):
        interval = n // 2
        while interval > 0:
            for i in range(interval, n):
                temp = array[i]
                j = i
                while j >= interval and array[j - interval] > temp:
                    array[j] = array[j - interval]
                    j -= interval

                array[j] = temp
            interval //= 2

    def sort(self, arr):
        size = len(arr)
        try:
            self.shellSort(arr, size)
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