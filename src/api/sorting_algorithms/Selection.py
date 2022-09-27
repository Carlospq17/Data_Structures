from api.sorting_algorithms.SortInterface import SortInterface

class Selection(SortInterface):

    def selectionSort(self, array, size):
        for step in range(size):
            min_idx = step
            for i in range(step + 1, size):
                if array[i] < array[min_idx]:
                    min_idx = i
            (array[step], array[min_idx]) = (array[min_idx], array[step])

    def sort(self, arr):
        size = len(arr)
        try:
            self.selectionSort(arr, size)
        except:
            print("Something went really wrong")
            print("This should be a Log error message")
        return arr
