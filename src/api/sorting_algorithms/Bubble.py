from api.sorting_algorithms.SortInterface import SortInterface
from random import randint

class Bubble(SortInterface):

    def sort(self, arr):
        try:
            for i in range(len(arr)):
                for j in range(0, len(arr) - i - 1):
                    if arr[j] > arr[j + 1]:
                        temp = arr[j]
                        arr[j] = arr[j+1]
                        arr[j+1] = temp
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