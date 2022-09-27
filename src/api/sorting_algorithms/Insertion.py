from api.sorting_algorithms.SortInterface import SortInterface

class Insertion(SortInterface):

    def sort(self, arr):
        try:
            for step in range(1, len(arr)):
                key = arr[step]
                j = step - 1        
                while j >= 0 and key < arr[j]:
                    arr[j + 1] = arr[j]
                    j = j - 1            
                arr[j + 1] = key
        except:
            print("Something went really wrong")
            print("This should be a Log error message")
        finally:
            return arr
