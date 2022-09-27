from api.sorting_algorithms.SortInterface import SortInterface

class Radix(SortInterface):

    def countingSort(self, array, place):
        size = len(array)
        output = [0] * size
        count = [0] * 10

        for i in range(0, size):
            index = array[i] // place
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = size - 1
        while i >= 0:
            index = array[i] // place
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(0, size):
            array[i] = output[i]


    def sort(self, arr):
        max_element = max(arr)
        place = 1
        
        try:
            while max_element // place > 0:
                self.countingSort(arr, place)
                place *= 10
        except:
            print("Something went really wrong")
            print("This should be a Log error message")
        finally:
            return arr